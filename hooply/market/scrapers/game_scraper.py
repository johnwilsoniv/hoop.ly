from hooply.logger import setup_logger
from hooply.market.scrapers.scraper import Scraper, ScrapeResult, ScrapeType

logger = setup_logger(__name__)

# class GameScraper(Scraper):
#     def scrape(self) -> Tuple[List[List[str]], Dict[str, list], Dict[str, list]]:
#         soup = self.request()
#
#         game_information = self._extract_game(soup)
#         teams_four_factors = self._extract_four_factors(soup)
#         teams = list(teams_four_factors.keys())
#         player_box_scores = self._extract_player_factors(soup, teams)
#
#         return game_information, teams_four_factors, player_box_scores
#
#     def _extract_game(self, soup: bs4.BeautifulSoup) -> List[List[str]]:
#         logger.info("Extracting game information.")
#         res = []
#         scorebox = soup.find("div", class_="scorebox")
#         away_team_div, home_team_div, meta = list(scorebox.children)
#         for team_div in [home_team_div, away_team_div]:
#             team_info_block, score_div, record_div, _ = list(team_div.children)
#             team, score, record = team_info_block.find("strong").find("a").text, score_div.text, record_div.text
#             res.append([team, score, record])
#
#         return res
#
#     def _extract_four_factors(self, soup: bs4.BeautifulSoup) -> Dict[str, List]:
#         logger.info("Extracting team four factors.")
#         res = {}
#         four_factors = soup.find("div", id="all_four_factors")
#         _, _, four_factors_comment = list(four_factors.children)
#
#         four_factors_table = BeautifulSoup(four_factors_comment, "html.parser")
#
#         for row in four_factors_table.find("tbody").children:
#             four_factors_html = list(row.children)
#             values = [
#                 four_factors_html[0].text,
#                 four_factors_html[1].text,
#                 four_factors_html[2].text,
#                 four_factors_html[6].text,
#             ]
#             logger.info("Team four factors: (%s).", values)
#             res[values[0]] = values[1:]
#
#         return res
#
#     def _extract_player_factors(self, soup: bs4.BeautifulSoup, teams: List[str]) -> Dict[str, List]:
#         res = {}
#         logger.info("Extracting player box score records.")
#         for team in teams:
#             res[team] = []
#             table_id = "box-{0}-game-basic".format(team)
#             team_box_score_table = soup.find(id=table_id)
#             box_score_rows = list(team_box_score_table.find("tbody").children)
#             for row in box_score_rows:
#                 # Skip separator
#                 if row.attrs.get("class", None) == ["thead"]:
#                     logger.info("Skipping player ingestion since 'thead' was found.")
#                     continue
#                 bs_tags = list(row.children)
#                 # DNP / Injury Case
#                 if bs_tags[1].get("data-stat") == "reason":
#                     values = [bs_tags[0].text]
#                 else:
#                     values = []
#                     for tag in bs_tags:
#                         # Extract all box score values minus percentages
#                         if "pct" not in tag.get("data-stat"):
#                             values.append(tag.text)
#
#                 logger.info("Box score record: (%s).", values)
#                 res[team].append(values)
#
#             # Extract inactive players
#             bottom_nav = soup.find(id="bottom-nav")
#             previous = bottom_nav.previous_sibling
#             # Check inactive row tbd.
#
#         return res