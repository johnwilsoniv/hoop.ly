from dataclasses import dataclass
from enum import Enum, auto
from os import path
from typing import List, Type

from bs4 import BeautifulSoup
from requests import Session
from requests.exceptions import RequestException

from hooply.logger import setup_logger
from hooply.market.pipeline import (
    DEFAULT_HOST,
    DEFAULT_REQUEST_HEADERS,
    DEFAULT_REQUEST_TIMEOUT,
)

logger = setup_logger(__name__)


class RequestResources(Enum):
    BOXSCORES = "boxscores"
    PLAYERS = "players"
    TEAMS = "teams"


class ScrapeResultType(Enum):
    multiple_games_link = auto()
    player = auto()
    game = auto()
    teams_boxscore = auto()
    players_boxscore = auto()


@dataclass
class ScrapeResult:
    result_type: ScrapeResultType
    data: List[Type]


class Scraper:
    def __init__(self, resource, params=None, headers=None, timeout=None):
        if params is None:
            params = dict()
        if headers is None:
            headers = DEFAULT_REQUEST_HEADERS
        if timeout is None:
            timeout = DEFAULT_REQUEST_TIMEOUT

        self.url = path.join(DEFAULT_HOST, resource)
        self.params = params
        self.headers = headers
        self.timeout = timeout

    def scrape(self) -> List[ScrapeResult]:
        raise NotImplementedError

    def request(self) -> BeautifulSoup:
        try:
            logger.info(
                "Requesting resource: (%s), (%s), (%s).",
                self.url,
                self.params,
                self.headers,
            )
            s = Session()
            resp = s.get(
                url=self.url,
                params=self.params,
                timeout=self.timeout,
                headers=self.headers,
            )
        except RequestException as e:
            logger.error(e)
            exit(1)

        html = "".join(line.strip() for line in resp.text.split("\n"))
        return BeautifulSoup(html, "html.parser")
