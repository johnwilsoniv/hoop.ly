from hooply.logger import setup_logger
from hooply.market.scrapers.scraper import Scraper, ScrapeResult, ScrapeResultType

logger = setup_logger(__name__)


class DateScraper(Scraper):
    def scrape(self) -> ScrapeResult:
        soup = self.request()
        data = []

        games = soup.find_all("div", class_="game_summary")
        logger.info("(%s) games were found.", len(games))

        if games:
            games = soup.find_all("div", class_="game_summary")
            for game in games:
                game_links = game.find("p", class_="links")
                boxscore_anchor, _, _, _, _ = list(game_links.children)
                link = boxscore_anchor.get("href").split("/")[-1]
                logger.info("Game link found: (%s)", link)
                data.append(link)
        return ScrapeResult(resource=ScrapeResultType.games_today, data=data)

    @staticmethod
    def generate_params(date: str):
        raise NotImplementedError
