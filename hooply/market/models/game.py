from peewee import *
from hooply.market import db


class Game(Model):
    id = AutoField()
    name = TextField()
    date = TimestampField()
    home_team = TextField()
    away_team = TextField()

    class Meta:
        database = db
        table_name = "game"
