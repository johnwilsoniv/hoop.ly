from typing import List, Dict

from bs4 import BeautifulSoup
from hooply.logger import setup_logger
from hooply.market.scrapers.scraper import Scraper, ScrapeResult, ScrapeResultType, RequestResources

logger = setup_logger(__name__)
PLAYER_BOX_SCORE_SIZE = 18


class GameScraper(Scraper):
    def scrape(self) -> List[ScrapeResult]:
        soup = self.request()

        game_information = self._extract_game(soup)
        teams_four_factors = self._extract_four_factors(soup)
        teams = list(teams_four_factors.keys())
        player_box_scores = self._extract_player_factors(soup, teams)

        sr_game_info = ScrapeResult(ScrapeResultType.game, game_information)
        sr_team_bs_info = ScrapeResult(ScrapeResultType.teams_boxscore, teams_four_factors)
        sr_player_bs_info = ScrapeResult(ScrapeResultType.players_boxscore, player_box_scores)

        return [sr_game_info, sr_team_bs_info, sr_player_bs_info]

    def _extract_game(self, soup: BeautifulSoup) -> List[List[str]]:
        logger.info("Extracting game information.")
        res = []
        scorebox = soup.find("div", class_="scorebox")
        away_team_div, home_team_div, meta = list(scorebox.children)
        for team_div in [home_team_div, away_team_div]:
            team_info_block, score_div, record_div, _ = list(team_div.children)
            team, score, record = team_info_block.find("strong").find("a").text, score_div.text, record_div.text
            res.append([team, score, record])

        return res

    def _extract_four_factors(self, soup: BeautifulSoup) -> Dict[str, list]:
        logger.info("Extracting team four factors.")
        res = {}
        four_factors = soup.find("div", id="all_four_factors")
        _, _, four_factors_comment = list(four_factors.children)

        four_factors_table = BeautifulSoup(four_factors_comment, "html.parser")

        for row in four_factors_table.find("tbody").children:
            four_factors_html = list(row.children)
            team, pace, efg, ortg = four_factors_html[0].text, four_factors_html[1].text, four_factors_html[2].text, four_factors_html[6].text,
            logger.info("Team four factors: (%s).", [team, pace, efg, ortg])
            res[team] = [pace, efg, ortg]

        return res

    def _extract_player_factors(self, soup: BeautifulSoup, teams: List[str]) -> Dict[str, list]:
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

                # Add filler values for players who didnt play
                values += ['0'] * (PLAYER_BOX_SCORE_SIZE - len(values))
                logger.info("Box score record: (%s).", values)
                res[team].append(values)

            # Extract inactive players: TO-DO
        return res

    @staticmethod
    def generate_resource(game_link: str):
        return f'{RequestResources.BOXSCORES.value}/{game_link}'
