import peewee
from peewee import Database, MySQLDatabase
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.game_team import GameTeamBoxscore
from hooply.market.models.game import Game
from hooply.market.models.player import Player
from hooply.market.models.base import db

MODELS = (Game, GamePlayerBoxscore, GameTeamBoxscore)


def init_db() -> Database:
    db.drop_tables(MODELS)
    db.create_tables(MODELS)
    return db
