from hooply.market.models.base import BaseModel
from peewee import AutoField, TextField, DecimalField, IntegerField


class GamePlayerBoxscore(BaseModel):
    id = AutoField()
    # Replace with backref key
    player_id = IntegerField()
    team = TextField()
    mp = DecimalField()
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
