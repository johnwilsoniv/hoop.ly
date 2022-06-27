from pandas import Timestamp
from typing import Dict, List
# from bs4 import B
from hooply.logger import setup_logger
from hooply.market.scrapers.scraper import Scraper, ScrapeResult, ScrapeResultType, RequestResources

logger = setup_logger(__name__)


class DateScraper(Scraper):


    def _extract_game(self, game) -> str:
        game_links = game.find("p", class_="links")
        boxscore_anchor, _, _, _, _ = list(game_links.children)
        link = boxscore_anchor.get("href").split("/")[-1]
        logger.info("Game link found: (%s)", link)

        return link

    def scrape(self) -> List[ScrapeResult]:
        soup = self.request()
        data = []

        games = soup.find_all("div", class_="game_summary")
        logger.info("(%s) games were found.", len(games))

        for game in games:
            link = self._extract_game(game)
            data.append(link)

        return [ScrapeResult(result_type=ScrapeResultType.multiple_games_link, data=data)]

    @staticmethod
    def generate_params(date: Timestamp) -> Dict[str, str]:
        return {
            "month": str(date.month),
            "day": str(date.day),
            "year": str(date.year)
        }

    @staticmethod
    def generate_resource() -> str:
        return RequestResources.BOXSCORES.value
