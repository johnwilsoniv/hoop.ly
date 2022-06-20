from hooply.market.pipeline.scraper import GameScraper
from hooply.market.models.game_team import GameTeamBoxscore
from hooply.market.models.game_player import GamePlayerBoxscore

DEFAULT_SLEEP_TIMEOUT = 5


def load_game_boxscore(start_date, end_date=None) -> None:
    pass
    # p = {
    #     "month": "10",
    #     "day": "20",
    #     "year": "2021"
    # }
    # ds = DateScraper(resource=Resources.BOXSCORES.value, params=p)
    # ds.scrape()

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


def load_teams() -> None:
    pass


def load_players() -> None:
    pass


if __name__ == '__main__':
    # Load all player / team / season data specified {cmd (click)}
    # Queue daily daily game update {cmd (click)}
    pass