from typing import List, Tuple, Type

from hooply.logger import setup_logger
from hooply.market.scrapers.scraper import (
    RequestResources,
    Scraper,
    ScrapeResult,
    ScrapeResultType,
)

logger = setup_logger(__name__)


class TeamRosterScraper(Scraper):
    def _extract_player(self, player_row: List[Type]) -> List[str]:
        (
            number_div,
            player_div,
            position_div,
            height_div,
            weight_div,
            _,
            _,
            _,
            _,
        ) = player_row

        # Extract player information from team
        player = player_div.find("a").text.strip()
        number = number_div.text.strip()
        position = position_div.text.strip()
        height = height_div.text.strip()
        weight = weight_div.text.strip()

        return [player, number, position, height, weight]

    def scrape(self) -> List[ScrapeResult]:
        soup = self.request()
        data = []

        roster_div = soup.find("div", id="div_roster")
        if roster_div is None:
            logger.error("Failed to retrieve roster div.")
            exit(1)

        roster_rows = list(roster_div.find("tbody").children)
        for row in roster_rows:
            player_info = self._extract_player(list(row.children))
            data.append(player_info)

        return [ScrapeResult(ScrapeResultType.player, data)]

    @staticmethod
    def generate_resource(team: str, season: str):
        return f"{RequestResources.TEAMS.value}/{team}/{season}.html"
