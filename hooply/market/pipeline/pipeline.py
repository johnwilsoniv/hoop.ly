from redis import Redis
from rq import Queue, Worker
from pandas import date_range
from hooply.market.pipeline import DEFAULT_QUEUE_NAME, DEV_SEASON_START, DEV_SEASON_END, TEAM_ABBREVIATIONS, DEFAULT_SEASON
from hooply.market.scrapers.team_scraper import TeamRosterScraper


def init_pipeline():
    # Initialize redis queue (if fresh is specified)
    #                         -> queue tasks
    #                          -> schedule periodic jobs
    # redis = Redis()
    # queue = Queue(DEFAULT_QUEUE_NAME)
    # preload_dates = date_range(DEV_SEASON_START, DEV_SEASON_END, freq='d').tolist()
    # print(preload_dates)
    # dates = DEV
    # queue = []

    # Load queue with job
    for team in TEAM_ABBREVIATIONS:
        resource = TeamRosterScraper.generate_resource(team, DEFAULT_SEASON)
        t = TeamRosterScraper(resource)
        res = t.scrape()
        print("here")

