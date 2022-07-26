import time

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
    PROD_TEAM_ABBREVIATIONS,
)
from hooply.market.scrapers.scraper import ScrapeResult
from hooply.market.pipeline.tasks import IngestTeamsTask, IngestGameTask, GetGamesTask
import os

logger = setup_logger(__name__)


def init_pipeline(db: Database) -> None:
    logger.info("Initializing data pipelines.")

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

    initial_dates = [GetGamesTask(date, db) for date in preload_dates]
    initial_teams = [IngestTeamsTask(team_abbreviations, season, db)]

    queue += initial_teams
    queue += initial_dates

    while queue:
        task = queue.pop(0)
        time.sleep(5)
        logger.info("Running task (%s)", task)
        res = task.run()

        if res is None:
            continue
        else:
            # Task has children
            if isinstance(task, GetGamesTask):
                ingest_game_tasks = []
                for game_link in res.data:
                    ingest_game_tasks.append(IngestGameTask(game_link, db))

                if ingest_game_tasks:
                    logger.info("Adding the following tasks into the queue: (%s)", ingest_game_tasks)
                    queue.extend(ingest_game_tasks)
