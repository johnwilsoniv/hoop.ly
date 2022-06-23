from redis import Redis
from rq import Queue, Worker
from pandas import date_range
from hooply.market.pipeline import DEFAULT_QUEUE_NAME, DEV_SEASON_START, DEV_SEASON_END, TEAM_ABBREVIATIONS, DEFAULT_SEASON
from hooply.market.scrapers.team_scraper import TeamRosterScraper
from hooply.market.pipeline.ingestion import DataLoader


def init_pipeline():
    # preload teams / players
    # Initialize redis queue (if fresh is specified)
    #                         -> queue tasks
    #                          -> schedule periodic jobs
    # redis = Redis()
    # queue = Queue(DEFAULT_QUEUE_NAME)
    # print(preload_dates)
    # dates = DEV
    # queue = []

    # Load queue with job
    for team in TEAM_ABBREVIATIONS:
        resource = TeamRosterScraper.generate_resource(team, DEFAULT_SEASON)
        t = TeamRosterScraper(resource)
        # sr = t.scrape()
        # DataLoader.load_team_roster(sr)

    preload_dates = date_range(DEV_SEASON_START, DEV_SEASON_END, freq='d').tolist()
    for date in preload_dates:
        print(date)