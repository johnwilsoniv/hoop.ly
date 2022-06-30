from peewee import AutoField, DecimalField, IntegerField, TextField, ForeignKeyField

from hooply.market.models.base import BaseModel
from hooply.market.models.player import Player


class GamePlayerBoxscore(BaseModel):
    id = AutoField()
    player_id = ForeignKeyField(Player, backref='player')
    team = TextField()
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
