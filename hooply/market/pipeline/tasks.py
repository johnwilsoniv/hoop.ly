from typing import Protocol, List
from peewee import Database
from pandas import Timestamp
from hooply.market.scrapers.date_scraper import DateScraper
from hooply.market.scrapers.game_scraper import GameScraper
from hooply.market.scrapers.team_scraper import TeamRosterScraper
from hooply.market.processors.bipm import BIPMProcessor
from hooply.market.pipeline.data_loader import DataLoader


class IngestionTask(Protocol):
    def run(self):
        pass


class IngestGameTask(IngestionTask):

    def __init__(self, date: Timestamp, db: Database):
        self.date = date
        self.db = db
        self.processor = BIPMProcessor()
        self.loader = DataLoader()

    def run(self) -> None:
        # Scrape the games for the given date
        resource = DateScraper.generate_resource()
        params = DateScraper.generate_params(self.date)
        d = DateScraper(resource=resource, params=params)
        [sr] = d.scrape()

        for game_link in sr.data:
            # Scrape box score from each game
            resource = GameScraper.generate_resource(game_link)
            g = GameScraper(resource=resource)
            _, team_bs_info_sr, player_bs_info_sr = g.scrape()
            # DataLoader.load_game(team_bs_info_sr, player_bs_info_sr, self.db)


class IngestTeamsTask(IngestionTask):
    def __init__(self, teams:List[str], season: str, db: Database):
        self.teams = teams
        self.season = season
        self.db = db
        self.loader = DataLoader()

    def run(self):
        for team in self.teams:
            resource = TeamRosterScraper.generate_resource(team, self.season)
            t = TeamRosterScraper(resource)
            (sr,) = t.scrape()
            self.loader.load_team_roster(sr, self.db)


# class IngestPlayerPosition(IngestionTask):
#     def run(self):
#         print("Hello")
