from models.query import (
    ActivePlayersQuery,
    BoxScoreTraditionalV2Query,
    LeagueGameFinderQuery,
)
from models.data_models import (
    Player
)
from hooply.market.logger import setup_logger
import pandas as pd

logger = setup_logger(__name__)


def populate_active_players():
    params = {
        "IsOnlyCurrentSeason": "1",
        "LeagueID": "00",
        "Season": "2021-22"
    }
    q = ActivePlayersQuery(params)
    result_set, columns = q.get()
    
    active_players_df = pd.DataFrame(data=result_set, columns=columns)
    # Filtering for the fields we need for player objects
    active_players_df = active_players_df[['DISPLAY_FIRST_LAST', 'PERSON_ID', 'TEAM_ID']]

    active_players = []
    for row in list(active_players_df.itertuples(index=False, name=None)):
        active_players.append(Player(name=row[0], player_id=row[1], team_id=row[2]))
    print(active_players)


if __name__ == "__main__":
    # params = {
    #     "IsOnlyCurrentSeason": "1",
    #     "LeagueID": "00",
    #     "Season": "2021-22"
    # }
    # q = ActivePlayersQuery(params)
    # params = {
    #     "EndPeriod": "1",
    #     "EndRange": "0",
    #     "GameID": "0042100307",
    #     "RangeType": "0",
    #     "StartPeriod": "1",
    #     "StartRange": "0"
    # }
    # q = BoxScoreTraditionalV2Query(params)
    # params = {"DataFrom": "01/09/2022", "PlayerOrTeam": "T", "LeagueID": "00"}
    # q = LeagueGameFinderQuery(params)
    # q.get()
    populate_active_players()
