from peewee import AutoField, DecimalField, ForeignKeyField, IntegerField, TextField

from hooply.market.models.base import BaseModel
from hooply.market.models.game import Game, Team
from hooply.market.models.player import Player


class GamePlayerBoxscore(BaseModel):
    id = AutoField()
    player = ForeignKeyField(Player, backref="player")
    game = ForeignKeyField(Game, backref="game")
    team = ForeignKeyField(Team, backref="team")
    mp = TextField()
    fg = IntegerField()
    fga = IntegerField()
    tpg = IntegerField()
    tpa = IntegerField()
    ft = IntegerField()
    fta = IntegerField()
    orb = IntegerField()
    drb = IntegerField()
    ast = IntegerField()
    stl = IntegerField()
    blk = IntegerField()
    tov = IntegerField()
    pf = IntegerField()
    pts = IntegerField()
    pm = IntegerField()
