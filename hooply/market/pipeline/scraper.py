from typing import List, Tuple, Dict

import bs4.element
from bs4 import BeautifulSoup
from hooply.market.logger import setup_logger
from requests import Session
from requests.exceptions import RequestException
from enum import Enum
from os import path

DEFAULT_REQUEST_HEADERS = {}
DEFAULT_REQUEST_TIMEOUT = 1
DEFAULT_HOST = "https://www.basketball-reference.com"


class Resources(Enum):
    BOXSCORES = "boxscores"
    PLAYERS = "players"


logger = setup_logger(__name__)


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

    def scrape(self):
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


class DateScraper(Scraper):
    def scrape(self):
        soup = self.request()
        res = []

        games = soup.find_all("div", class_="game_summary")
        logger.info("(%s) games were found.", len(games))

        if games:
            games = soup.find_all("div", class_="game_summary")
            for game in games:
                game_links = game.find("p", class_="links")
                boxscore_anchor, _, _, _, _ = list(game_links.children)
                link = boxscore_anchor.get("href").split("/")[-1]
                logger.info("Game link found: (%s)", link)
                res.append(link)
        return res


class GameScraper(Scraper):
    def scrape(self):
        soup = self.request()

        teams_four_factors = self._extract_four_factors(soup)
        teams = list(teams_four_factors.keys())
        player_box_scores = self._extract_player_factors(soup, teams)

        return teams_four_factors, player_box_scores

    def _extract_four_factors(self, soup: bs4.BeautifulSoup) -> Dict[str, List]:
        logger.info("Extracting team four factors.")
        res = {}
        four_factors = soup.find("div", id="all_four_factors")
        _, _, four_factors_comment = list(four_factors.children)

        four_factors_table = BeautifulSoup(four_factors_comment, "html.parser")

        for row in four_factors_table.find("tbody").children:
            four_factors_html = list(row.children)
            values = [
                four_factors_html[0].text,
                four_factors_html[1].text,
                four_factors_html[2].text,
                four_factors_html[6].text,
            ]
            logger.info("Team four factors: (%s).", values)
            res[values[0]] = values[1:]

        return res

    def _extract_player_factors(self, soup: bs4.BeautifulSoup, teams: List[str]) -> Dict[str, List]:
        res = {}
        logger.info("Extracting player box score records.")
        for team in teams:
            res[team] = []
            table_id = "box-{0}-game-basic".format(team)
            team_box_score_table = soup.find(id=table_id)
            box_score_rows = list(team_box_score_table.find("tbody").children)
            for row in box_score_rows:
                # Skip separator
                if row.attrs.get("class", None) == ["thead"]:
                    logger.info("Skipping player ingestion since 'thead' was found.")
                    continue
                bs_tags = list(row.children)
                # DNP / Injury Case
                if bs_tags[1].get("data-stat") == "reason":
                    values = [bs_tags[0].text]
                else:
                    values = []
                    for tag in bs_tags:
                        # Extract all box score values minus percentages
                        if "pct" not in tag.get("data-stat"):
                            values.append(tag.text)

                logger.info("Box score record: (%s).", values)
                res[team].append(values)
        return res


if __name__ == "__main__":
    print("Hello World")
