from models.query import ActivePlayersQuery, BoxScoreTraditionalV2Query, LeagueGameFinderQuery
import logging

DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname) -7s " "%(name)s: %(message)s"
DEFAULT_LOG_LEVEL = logging.DEBUG
DEFAULT_LOG_FILE = 'app.log'

logging.basicConfig(level=DEFAULT_LOG_LEVEL, format=DEFAULT_LOG_FORMAT)

if __name__ == '__main__':
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
    params = {
        "DataFrom": "01/09/2022",
        "PlayerOrTeam": "T",
        "LeagueID": "00"
    }
    q = LeagueGameFinderQuery(params)
    q.get()
