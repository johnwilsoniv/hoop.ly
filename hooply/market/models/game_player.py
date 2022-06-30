from peewee import AutoField, DecimalField, IntegerField, TextField

from hooply.market.models.base import BaseModel


class GamePlayerBoxscore(BaseModel):
    id = AutoField()
    # Replace with backref key
    # player_id = IntegerField()
    player = TextField()
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
