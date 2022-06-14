from peewee import *
from hooply.market import db


class Player(Model):
    name = TextField()
    slug = TextField()
    position = TextField()
    height = TextField()
    weight = TextField()

    class Meta:
        database = db
        table_name = "player"
