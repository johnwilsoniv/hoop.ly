import peewee
from peewee import Database, MySQLDatabase
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.game_team import GameTeamBoxscore
from hooply.market.models.game import Game
from hooply.market.models.player import Player
from hooply.market.models.meta_ingestion import MetaIngestion
from hooply.market.models.base import db
from hooply.logger import setup_logger

MODELS = (Game, GamePlayerBoxscore, GameTeamBoxscore, Player, MetaIngestion)
logger = setup_logger(__name__)


def init_db(truncate=True) -> Database:
    logger.info("Initializing data models.")
    if truncate:
        db.drop_tables(MODELS)
        db.create_tables(MODELS)
    return db
