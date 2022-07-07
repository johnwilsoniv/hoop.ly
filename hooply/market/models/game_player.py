from peewee import AutoField, DecimalField, IntegerField, TextField, ForeignKeyField

from hooply.market.models.base import BaseModel
from hooply.market.models.player import Player
from hooply.market.models.game import Game
from hooply.market.models.game import Team


class GamePlayerBoxscore(BaseModel):
    id = AutoField()
    player_id = ForeignKeyField(Player, backref='player')
    game_id = ForeignKeyField(Game, backref='game')
    team_id = ForeignKeyField(Team, backref='team')
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
