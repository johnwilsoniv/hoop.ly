from typing import List, Protocol, runtime_checkable, Type
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.game_team import GameTeamBoxscore


@runtime_checkable
class Processor(Protocol):
    def calculate_score(
        self,
        player_boxscores: List[GamePlayerBoxscore],
        team_boxscore: List[GameTeamBoxscore],
    ) -> List[Type]:
        ...


class BIPMProcessor(Processor):
    def calculate_score(
        self,
        player_boxscores: List[GamePlayerBoxscore],
        team_boxscore: List[GameTeamBoxscore],
    ) -> List[Type]:
        return []
