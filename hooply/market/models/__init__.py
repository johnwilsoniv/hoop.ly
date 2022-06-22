import peewee
from peewee import Database, MySQLDatabase
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.game_team import GameTeamBoxscore
from hooply.market.models.game import Game

MODELS = (Game, GamePlayerBoxscore, GameTeamBoxscore)

def init_db() -> Database:
    db = MySQLDatabase(
        database="hooply",
        host="localhost",
        port=3306,
        user="root",
        password="test",
        # pragmas={"journal_mode": "wal", "cache_size": 10000, "foreign_keys": 1},
    )
    return db
