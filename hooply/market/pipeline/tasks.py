from typing import Protocol, Dict, runtime_checkable, Any
from peewee import Database
from pandas import Timestamp
from hooply.market.scrapers.date_scraper import DateScraper
from hooply.market.scrapers.game_scraper import GameScraper
from hooply.market.scrapers.team_scraper import TeamRosterScraper
from hooply.market.processors.bipm import BIPMProcessor
from hooply.market.pipeline.data_loader import DataLoader


@runtime_checkable
class Task(Protocol):
    def run(self):
        pass


class GetGamesTask(Task):

    def __init__(self, date: Timestamp, db: Database):
        self.date = date
        self.db = db
        self.processor = BIPMProcessor()
        self.loader = DataLoader()

    def run(self) -> Any:
        # Scrape the games for the given date
        resource = DateScraper.generate_resource()
        params = DateScraper.generate_params(self.date)
        d = DateScraper(resource=resource, params=params)
        [sr] = d.scrape()

        return sr


class IngestGameTask(Task):

    def __init__(self, game_link: str, db: Database):
        self.game_link = game_link
        self.db = db
        self.processor = BIPMProcessor()
        self.loader = DataLoader()

    def run(self) -> Any:
        # Scrape box score from each game
        resource = GameScraper.generate_resource(self.game_link)
        g = GameScraper(resource=resource)
        game_info_sr, team_bs_info_sr, player_bs_info_sr = g.scrape()
        game = self.loader.load_game(game_info_sr, team_bs_info_sr, player_bs_info_sr, self.db)

        # Add BIPMs for game
        player_bs_bipms = self.processor.calculate_score(game)
        self.loader.load_bipm(player_bs_bipms, self.db)


class IngestTeamsTask(Task):
    def __init__(self, teams: Dict[str, str], season: str, db: Database):
        self.teams = teams
        self.season = season
        self.db = db
        self.loader = DataLoader()

    def run(self):
        # Load all teams
        self.loader.load_teams(self.teams, self.db)

        # Load all players currently on a roster
        for team in self.teams:
            resource = TeamRosterScraper.generate_resource(team, self.season)
            t = TeamRosterScraper(resource)
            (sr,) = t.scrape()
            self.loader.load_team_roster(sr, self.db)
