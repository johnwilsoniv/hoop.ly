from hooply.market.pipeline.scraper import GameScraper, DateScraper, Resources
from hooply.market.models.game_team import GameTeamBoxscore
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.logger import setup_logger
from hooply.market import db
from datetime import date
from time import sleep
from os import path

DEFAULT_SLEEP_TIMEOUT = 5
logger = setup_logger(__name__)


# def _load_game():
#     with db.atomic() as game_txn:
#         # do stuff
#         pass
#
#         with db.atomic() as boxscore_txn:
#             pass


# def load_date_boxscore(d: date) -> None:
#     year, month, day = d.isoformat().split("-")
#     params = {
#         "month": month,
#         "day": day,
#         "year": year
#     }
#     ds = DateScraper(resource=Resources.BOXSCORES.value, params=params)
#     game_links = ds.scrape()
#
#     if not game_links:
#         logger.info("No data ingested for date: (%s).", d)
#         return
#
#     for gl in game_links[0:1]:
#         s = GameScraper(path.join(Resources.BOXSCORES.value, gl))
#         game_information, team_boxscore, player_boxscore = s.scrape()
#         # _load_game()
#         sleep(DEFAULT_SLEEP_TIMEOUT)

        # # load_player_boxscore(player_boxscore)
        # load_team_boxscore(team_boxscore)

    # gl = "202110200CHO.html"
    # s = GameScraper(path.join(Resources.BOXSCORES.value, gl))
    # s.scrape()

    # s = DateScraper(params={
    #     "month": "10",
    #     "day": "20",
    #     "year": "2021"
    # })

    # Generate all dates between start and end
    # For each -> Date Scrape, if games -> generate all Game Scraper params -> Game Scrape -> save


# def load_teams() -> None:
#     pass
#
#
# def load_players() -> None:
#     pass


if __name__ == '__main__':
    # Load all player / team / season data specified {cmd (click)}
    # Queue daily daily game update {cmd (click)}
    # d = date(2022, 6, 16)
    # load_date_boxscore(d)
    print("Hello world")