from typing import List

from hooply.logger import setup_logger
from hooply.market.scrapers.scraper import Scraper, ScrapeResult, ScrapeResultType, RequestResources

logger = setup_logger(__name__)


class TeamRosterScraper(Scraper):
    def scrape(self) -> List[ScrapeResult]:
        soup = self.request()
        data = []

        roster_div = soup.find("div", id="div_roster")
        if roster_div is None:
            logger.error("Failed to retrieve roster div.")
            exit(1)

        roster_rows = list(roster_div.find("tbody").children)
        for player_row in roster_rows:
            number_div, player_div, position_div, height_div, weight_div, _, _, _, _ = list(player_row.children)

            # Extract player information from team
            player = player_div.find("a").text.strip()
            number = number_div.text.strip()
            position = position_div.text.strip()
            height = height_div.text.strip()
            weight = weight_div.text.strip()

            data.append((player, number, position, height, weight))

        return [ScrapeResult(ScrapeResultType.player, data)]

    @staticmethod
    def generate_resource(team: str, season: str):
        return f'{RequestResources.TEAMS.value}/{team}/{season}.html'
