from typing import List, Protocol
from hooply.market.models.scores import Scores
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.game_team import GameTeamBoxscore


class Processor(Protocol):

    def calculate_score(self, player_boxscores: List[GamePlayerBoxscore], team_boxscore: List[GameTeamBoxscore]) -> List[Scores]:
        pass


class BIPMProcessor(Processor):
    def calculate_score(self, player_boxscores: List[GamePlayerBoxscore], team_boxscore: List[GameTeamBoxscore]) -> List[Scores]:
        pass