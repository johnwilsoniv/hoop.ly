from pandas import date_range
from peewee import Database
from redis import Redis
from rq import Queue, Worker

from hooply.logger import setup_logger
from hooply.market.pipeline import (
    DEFAULT_QUEUE_NAME,
    DEV_SEASON,
    DEV_SEASON_END,
    DEV_SEASON_START,
    DEV_TEAM_ABBREVIATIONS,
)
from hooply.market.pipeline.data_loader import DataLoader
from hooply.market.scrapers.date_scraper import DateScraper
from hooply.market.scrapers.game_scraper import GameScraper
from hooply.market.scrapers.scraper import ScrapeResult, ScrapeResultType
from hooply.market.scrapers.team_scraper import TeamRosterScraper

logger = setup_logger(__name__)


def ingest_team_roster(team: str, season: str, db: Database) -> None:
    resource = TeamRosterScraper.generate_resource(team, season)
    t = TeamRosterScraper(resource)
    (sr,) = t.scrape()
    DataLoader.load_team_roster(sr, db)


def ingest_games_in_range(
    start_date: str, end_date: str, db: Database
) -> None:
    preload_dates = date_range(start_date, end_date, freq="d").tolist()
    for date in preload_dates:
        resource = DateScraper.generate_resource()
        params = DateScraper.generate_params(date)
        d = DateScraper(resource=resource, params=params)
        [sr] = d.scrape()

        for game_link in sr.data:
            resource = GameScraper.generate_resource(game_link)
            g = GameScraper(resource=resource)
            game_bs_info_sr, team_bs_info_sr, player_bs_info_sr = g.scrape()
            DataLoader.load_game(
                game_bs_info_sr, team_bs_info_sr, player_bs_info_sr, db
            )
            logger.info("Breaking after first game.")
            break


def init_pipeline(db: Database) -> None:
    logger.info("Initializing data pipeline.")
    # preload teams / players
    # Initialize redis queue (if fresh is specified)
    #                         -> queue tasks
    #                          -> schedule periodic jobs
    # redis = Redis()
    # queue = Queue(DEFAULT_QUEUE_NAME)
    # print(preload_dates)
    # dates = DEV
    # queue = []

    # Load initial teams
    DataLoader.load_teams(DEV_TEAM_ABBREVIATIONS, db)

    # Load initial players
    for team in DEV_TEAM_ABBREVIATIONS:
        ingest_team_roster(team, DEV_SEASON, db)

    ingest_games_in_range(DEV_SEASON_START, DEV_SEASON_END, db)
