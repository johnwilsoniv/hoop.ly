from hooply.market.processors.processor import Processor
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.game_team import GameTeamBoxscore
from hooply.market.models.game_team import Game
from hooply.market.processors.coefficient import Coefficient
from hooply.market.processors import *
from typing import List, Type, Tuple, Any
from operator import mul
from decimal import Decimal

PTS_COEFFICIENTS = Coefficient(*BIPM_PTS)
TPM_COEFFICIENTS = Coefficient(*BIPM_3PM)
AST_COEFFICIENTS = Coefficient(*BIPM_AST)
TO_COEFFICIENTS = Coefficient(*BIPM_TO)
ORB_COEFFICIENTS = Coefficient(*BIPM_ORB)
DRB_COEFFICIENTS = Coefficient(*BIPM_DRB)
STL_COEFFICIENTS = Coefficient(*BIPM_STL)
BLK_COEFFICIENTS = Coefficient(*BIPM_BLK)
PF_COEFFICIENTS = Coefficient(*BIPM_PF)

FGA_COEFFICIENTS = Coefficient(*BIPM_FGA)
FTA_COEFFICIENTS = Coefficient(*BIPM_FTA)

POS_MAP = {
    'PG': 1,
    'SG': 2,
    'SF': 3,
    'PF': 4,
    'C': 5
}

BASELINE_PTS_TSA = Decimal(1.00)


def calculate_tsa(fga: int, fta: int) -> Decimal:
    return Decimal(fga + FTA_VALUE * fta)


def adjust_pts(pts:Decimal, pts_tsa:Decimal, team_pts_tsa:Decimal, baseline_pts_tsa: Decimal):
    return pts + (baseline_pts_tsa - team_pts_tsa) * pts_tsa


def calculate_per_100(stat: Decimal, minutes: Decimal, pace: Decimal) -> Decimal:
    if minutes:
        per48 = stat / minutes * MPG
        res = per48 / pace * 100
    else:
        res = 0
    return res


def extract_minutes_played(s) -> Decimal:
    temp = s.split(":")
    if len(temp) == 1:
        res = 0
    else:
        res = Decimal(temp[0]) + Decimal(temp[1]) / 60
    return res


class BIPMProcessor:

    COEFFICIENTS = {
        'position': {
            'pts': PTS_COEFFICIENTS,
            'tpg': TPM_COEFFICIENTS,
            'ast': AST_COEFFICIENTS,
            'tov': TO_COEFFICIENTS,
            'orb': ORB_COEFFICIENTS,
            'drb': DRB_COEFFICIENTS,
            'stl': STL_COEFFICIENTS,
            'blk': BLK_COEFFICIENTS,
            'pf': PF_COEFFICIENTS,
        },
        'role': {
            'fga': FGA_COEFFICIENTS,
            'fta': FTA_COEFFICIENTS
        },
    }

    def _some_function(self, stats_per100: List, coefficients: List, stat_names: List[str], player_bs: GamePlayerBoxscore, role_or_position_name:str, mp: Decimal, pace: Decimal, team_pts_tsa: Decimal):
        for stat in stat_names:
            stat_bs = player_bs.__getattribute__(stat)
            if stat == 'pts':
                #Adjust pts for offensive role
                pts_tsa = calculate_tsa(player_bs.fga, player_bs.fta)
                stat_bs = adjust_pts(stat_bs, pts_tsa, team_pts_tsa, BASELINE_PTS_TSA)

            stat_per100 = calculate_per_100(stat_bs, mp, pace)
            # TO-DO: Use listed position as position/offensive role for now
            role_or_position = POS_MAP[player_bs.player.position]

            coefficient = BIPMProcessor.COEFFICIENTS[role_or_position_name][stat].get_coefficient(role_or_position)

            stats_per100.append(stat_per100)
            coefficients.append(coefficient)

    def raw_bpm(self, players_bs: List[GamePlayerBoxscore], team_bs: GameTeamBoxscore, team_pts_tsa: Decimal) -> List[
        Tuple[Any]]:

        raw_bpms = []
        for player_bs in players_bs:
            mp = extract_minutes_played(player_bs.mp)
            pace = Decimal(team_bs.pace)

            coefficients = []
            stats_per100 = []

            self._some_function(stats_per100, coefficients, BIPM_POS_STATS, player_bs, 'position', mp, pace, team_pts_tsa)
            self._some_function(stats_per100, coefficients, BIPM_ROLE_STATS, player_bs, 'role', mp, pace, None)

            raw_bpm_breakdown = list(map(mul, stats_per100, coefficients))
            raw_bpm = sum(raw_bpm_breakdown)
            raw_bpms.append((player_bs.player.name, player_bs.game.id, raw_bpm, mp))

        return raw_bpms


    def calculate_score(
        self,
        game: Game
    ) -> List[Type]:
        bpms = dict()

        team_bs_query = GameTeamBoxscore.select().where(GameTeamBoxscore.game_id == game.id)
        player_bs_query = GamePlayerBoxscore.select().where(GamePlayerBoxscore.game_id == game.id)

        teams_bs: List[GameTeamBoxscore] = [res for res in team_bs_query]
        teams_player_bs: List[List[GamePlayerBoxscore], GamePlayerBoxscore] = [[], []]

        # Extract player boxscores for each team
        for player_bs in player_bs_query:
            if player_bs.team_id == teams_bs[0].team_id:
                teams_player_bs[0].append(player_bs)
            else:
                teams_player_bs[1].append(player_bs)

        for i in range(2):
            # Calculate team true shooting attempts
            team_tsa = calculate_tsa(sum([t.fga for t in teams_player_bs[i]]), sum([t.fta for t in teams_player_bs[i]]))
            team_pts_tsa = teams_bs[i].pts / team_tsa

            raw_bpms = self.raw_bpm(teams_player_bs[i], teams_bs[i], team_pts_tsa)

        return []


if __name__ == '__main__':
    klay_coefficients = [0.860, 0.389, 0.767, -0.964, 0.435, 0.143, 0.000, 1.221, 1.071, -0.367, -0.677, -0.298]
    g = Game.select().where(Game.id == 1).get()
    b = BIPMProcessor()
    b.calculate_score(g)
