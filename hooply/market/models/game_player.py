from peewee import *
from hooply.market import db


class GamePlayerBoxscore(Model):
    id = AutoField()
    # Replace with backref key
    player_id = IntegerField()
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

    class Meta:
        database = db
        table_name = "game_player_boxscore"
