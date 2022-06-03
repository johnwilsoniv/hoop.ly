from abc import ABC, abstractmethod
from requests.sessions import Session
from hooply.market.logger import setup_logger

logger = setup_logger(__name__)

DEFAULT_HEADERS = {
    "Host": "stats.nba.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true",
    "Connection": "keep-alive",
    "Referer": "https://stats.nba.com/",
}


class StatsQuery(ABC):
    def __init__(self, resource, params=None, headers=None):
        if params is None:
            params = dict()
        if headers is None:
            headers = DEFAULT_HEADERS

        self.params = params
        self.headers = headers
        self.url = "https://stats.nba.com/stats/" + resource

    @abstractmethod
    def get(self):
        pass


class ActivePlayersQuery(StatsQuery):
    RESOURCE = "commonallplayers"

    def __init__(self, params):
        super().__init__(ActivePlayersQuery.RESOURCE, params)

    def get(self):
        try:
            # logger.info("Creating an active player request to (%s) with parameters (%s)", self.url)
            s = Session()
            resp = s.get(self.url, params=self.params, headers=self.headers)
            data = resp.json()
            records = data.get("resultSets")[0]
            columns, result_set = records.get("headers"), records.get("rowSet")
        except Exception as e:
            logger.error("Some error occurred...")
            logger.error(e)
            exit(1)
        finally:
            logger.info("Request completed.")
            return result_set, columns


class BoxScoreTraditionalV2Query(StatsQuery):
    RESOURCE = "boxscoretraditionalv2"

    def __init__(self, params):
        super().__init__(BoxScoreTraditionalV2Query.RESOURCE, params)

    def get(self):
        try:
            logger.info("")
            s = Session()
            resp = s.get(self.url, params=self.params, headers=self.headers)
            data = resp.json()
            records = data.get("resultSets")[0]
            columns, result_set = records.get("headers"), records.get("rowSet")
            print(result_set)
        except Exception as e:
            logger.error("Error case.")
            logger.error(e)
            exit(1)
        finally:
            logger.info("Request completed.")


class LeagueGameFinderQuery(StatsQuery):
    RESOURCE = "leaguegamefinder"

    def __init__(self, params):
        super().__init__(LeagueGameFinderQuery.RESOURCE, params)

    def get(self):
        try:
            logger.info("")
            s = Session()
            resp = s.get(self.url, params=self.params, headers=self.headers)
            data = resp.json()
            records = data.get("resultSets")[0]
            columns, result_set = records.get("headers"), records.get("rowSet")
            print(result_set[0])
        except Exception as e:
            logger.error("Error case.")
            logger.error(e)
            exit(1)
        finally:
            logger.info("Request completed.")
