from typing import List, Tuple, Dict

import bs4.element
from bs4 import BeautifulSoup
from hooply.market.logger import setup_logger
from requests import Session
from enum import Enum

DEFAULT_REQUEST_HEADERS = {}
DEFAULT_REQUEST_TIMEOUT = 1
HOST = "https://www.basketball-reference.com/"


class Resources(Enum):
    BOXSCORES = "boxscores"


logger = setup_logger(__name__)


class DateScraper:
    def __init__(self, params=None, headers=None, timeout=None):
        if params is None:
            params = dict()
        if headers is None:
            headers = DEFAULT_REQUEST_HEADERS
        if timeout is None:
            timeout = DEFAULT_REQUEST_TIMEOUT

        self.url = "https://www.basketball-reference.com/" + Resources.BOXSCORES.value
        self.params = params
        self.headers = headers
        self.timeout = timeout

    def scrape(self) -> List[str]:
        logger.info("Beginning to scrape.")
        res = []

        s = Session()
        resp = s.get(url=self.url, params=self.params, timeout=self.timeout, headers=self.headers)
        data = resp.text.encode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')

        games = soup.find_all("div", class_="game_summary")
        logger.info("(%s) games were found at target (%s) with params (%s).", len(games), self.url, self.params)

        if games:
            games = soup.find_all("div", class_="game_summary")
            for game in games:
                game_links = game.find("p", class_="links")
                boxscore_anchor, _, _, _, _ = list(game_links.children)
                link = boxscore_anchor.get("href").split("/")[-1]
                logger.info("Game link found: (%s)", link)

        return res


class GameScraper:
    def __init__(self, resource, params=None, headers=None, timeout=None):
        if params is None:
            params = dict()
        if headers is None:
            headers = DEFAULT_REQUEST_HEADERS
        if timeout is None:
            timeout = DEFAULT_REQUEST_TIMEOUT

        self.url = "https://www.basketball-reference.com/" + Resources.BOXSCORES.value + "/" + resource
        self.params = params
        self.headers = headers
        self.timeout = timeout

    def scrape(self) -> List[str]:
        logger.info("Beginning to scrape.")
        res = []

        s = Session()
        resp = s.get(url=self.url, params=self.params, timeout=self.timeout, headers=self.headers)
        data = resp.text.encode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')

        team_record = self.extract_four_factors(soup)
        player = self.extract_player_factors(soup, list(team_record.keys()))
        return res

    def extract_four_factors(self, soup: bs4.BeautifulSoup) -> Dict[str, Tuple]:
        """

        """
        res = {}
        four_factors = soup.find("div", id="all_four_factors")
        _, _, _, _, inner, _ = list(four_factors.children)
        # Remove whitespace and reload parser
        comment_text = inner.strip().replace("\n", "")
        four_factors_table = BeautifulSoup(comment_text, 'html.parser')
        for row in four_factors_table.find("tbody").children:
            four_factors_html = list(row.children)
            team, pace, efg, ortg = four_factors_html[0].text, four_factors_html[1].text, four_factors_html[2].text, \
                                    four_factors_html[6].text
            res[team] = (pace, efg, ortg)
        return res

    def extract_player_factors(self, soup: bs4.BeautifulSoup, teams: List[str]) -> None:
        for team in teams:
            table_id = "box-{0}-game-basic".format(team)
            team_box_score_table = soup.find(id="box-CHO-game-basic")
            box_score_rows = list(team_box_score_table.find("tbody").children)
            # if
            # for row in team_box_score_table.find("tbody").children:
            #     print(row)
        pass


#
#
# class PlayerScraper(Scraper):
#     pass


if __name__ == '__main__':
    # s = DateScraper(params={
    #     "month": "10",
    #     "day": "20",
    #     "year": "2021"
    # })
    s = GameScraper("202110200CHO.html")
    s.scrape()
