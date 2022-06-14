from peewee import *
from hooply.market import db


class Scores(Model):
    id = AutoField()
    type = TextField()
    value = DecimalField()

    class Meta:
        database = db
        table_name = "scores"
