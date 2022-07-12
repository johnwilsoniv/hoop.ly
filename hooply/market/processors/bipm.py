from hooply.market.processors.processor import Processor
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.game_team import GameTeamBoxscore
from hooply.market.models.game_team import Game
from hooply.market.processors.coefficient import Coefficient
from hooply.market.processors import *
from typing import List, Type
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

    def raw_bpm(self, player_bs: GamePlayerBoxscore, team_bs: GameTeamBoxscore) -> None:

        mp = extract_minutes_played(player_bs.mp)
        pace = Decimal(team_bs.pace)
        coefficients = []
        stats_per100 = []

        for stat in BIPM_POS_STATS:
            stat_per100 = calculate_per_100(player_bs.__getattribute__(stat), mp, pace)
            coefficient = BIPMProcessor.COEFFICIENTS['position'][stat].get_coefficient(2.6)

            stats_per100.append(stat_per100)
            coefficients.append(coefficient)

        for stat in BIPM_ROLE_STATS:
            stat_per100 = calculate_per_100(player_bs.__getattribute__(stat), mp, pace)
            coefficient = BIPMProcessor.COEFFICIENTS['role'][stat].get_coefficient(3.1)

            stats_per100.append(stat_per100)
            coefficients.append(coefficient)

        print()


    def calculate_score(
        self,
        game: Game
    ) -> List[Type]:
        bpms = dict()

        team_bs_query = GameTeamBoxscore.select().where(GameTeamBoxscore.game_id == game.id)
        player_bs_query = GamePlayerBoxscore.select().where(GamePlayerBoxscore.game_id == game.id)

        teams_bs: List[GameTeamBoxscore]  = [res for res in team_bs_query]
        player_bs: List[GamePlayerBoxscore] = [res for res in player_bs_query]

        for pbs in player_bs:
            #
            if pbs.team_id == teams_bs[0].team_id:
                tbs = teams_bs[0]
            else:
                tbs = teams_bs[1]

            raw_bpm = self.raw_bpm(pbs, tbs)

        return []


if __name__ == '__main__':
    klay_coefficients = [0.860, 0.389, 0.767, -0.964, 0.435, 0.143, 0.000, 1.221, 1.071, -0.367, -0.677, -0.298]
    g = Game.select().where(Game.id == 1).get()
    b = BIPMProcessor()
    b.calculate_score(g)
