from pandas import date_range
from peewee import Database
from hooply.logger import setup_logger
from hooply.market.pipeline import (
    DEFAULT_QUEUE_NAME,
    DEV_SEASON,
    DEV_SEASON_END,
    DEV_SEASON_START,
    DEV_TEAM_ABBREVIATIONS,
    PROD_SEASON,
    PROD_SEASON_START,
    PROD_SEASON_END,
    PROD_TEAM_ABBREVIATIONS,
)
from hooply.market.pipeline.data_loader import DataLoader
from hooply.market.scrapers.date_scraper import DateScraper
from hooply.market.scrapers.game_scraper import GameScraper
from hooply.market.scrapers.scraper import ScrapeResult, ScrapeResultType
from hooply.market.scrapers.team_scraper import TeamRosterScraper
from hooply.market.pipeline.tasks import IngestTeamsTask, IngestGameTask
import os


def init_pipeline(db: Database) -> None:

    if os.environ.get('ENV') == 'production':
        season = PROD_SEASON
        season_start = PROD_SEASON_START
        season_end = None
        team_abbreviations = PROD_TEAM_ABBREVIATIONS

    else:
        season = DEV_SEASON
        season_start = DEV_SEASON_START
        season_end = DEV_SEASON_END
        team_abbreviations = DEV_TEAM_ABBREVIATIONS

    # Setup initial taskse
    queue = []
    preload_dates = date_range(season_start, season_end, freq="d").tolist()
    initial_games = [IngestGameTask(date, db) for date in preload_dates]
    initial_teams = IngestTeamsTask(team_abbreviations, season, db)

    queue += [initial_games]
    queue += [initial_teams]

    while queue:
        task = queue.pop()
        task.run()
