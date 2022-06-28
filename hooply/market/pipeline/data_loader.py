from peewee import Database, DatabaseError
from hooply.logger import setup_logger
from hooply.market.scrapers.scraper import ScrapeResult, ScrapeResultType
from hooply.market.models.player import Player
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.game_team import GameTeamBoxscore
from hooply.market.models.meta_ingestion import MetaIngestion

DEFAULT_SLEEP_TIMEOUT = 5
logger = setup_logger(__name__)


class DataLoader:

    @staticmethod
    def load_game(team_sr: ScrapeResult, player_sr: ScrapeResult, db: Database) -> None:
        if team_sr.result_type != ScrapeResultType.teams_boxscore or player_sr.result_type != ScrapeResultType.players_boxscore:
            logger.error("Replace.")
            exit(1)

        with db.atomic() as txn:
            try:
                for team in team_sr.data:
                    pace, efg, ortg = team_sr.data[team]
                    gbs = GameTeamBoxscore.create(team=team, pace=pace, efg=efg, ortg=ortg)
                    logger.info("Created game boxscore record (%s)", gbs)
            except DatabaseError:
                txn.rollback()

        with db.atomic() as txn:
            try:
                for team in player_sr.data:
                    for player_bs in player_sr.data[team]:
                        name, mp, fg, fga, tpg, tpa, ft, fta, orb, drb, _, ast, stl, blk, tov, pf, pts, pm = player_bs
                        pbs = GamePlayerBoxscore.create(player=name, team=team, mp=min, fg=fg, fga=fga, tpg=tpg,
                                                        tpa=tpa,
                                                        ft=ft, fta=fta, orb=orb, drb=drb, ast=ast, stl=stl, blk=blk,
                                                        tov=tov,
                                                        pf=pf, pts=pts, pm=pm)
                        logger.info("Created player boxscore record (%s)", pbs)
            except DatabaseError:
                txn.rollback()

        with db.atomic() as txn:
            try:
                m = MetaIngestion.create(type="player_boxscore")
                logger.info("Created meta ingestion record (%s)", m)
                txn.commit()
            except DatabaseError:
                txn.rollback()

    @staticmethod
    def load_team_roster(s: ScrapeResult, db: Database) -> None:
        if s.result_type != ScrapeResultType.player:
            logger.error("Replace.")
            exit(1)

        with db.atomic() as txn:
            try:
                for player in s.data:
                    name, _, position, height, weight = player
                    p = Player.create(name=name, position=position, height=height, weight=weight)
                    logger.info("Created player (%s)", p)
                txn.commit()
            except DatabaseError:
                txn.rollback()

        with db.atomic() as txn:
            try:
                m = MetaIngestion.create(type="player")
                logger.info("Created meta ingestion record (%s)", m)
                txn.commit()
            except DatabaseError:
                txn.rollback()

    @staticmethod
    def _load_bipm(s: ScrapeResult) -> None:
        raise NotImplementedError

