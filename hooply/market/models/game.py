from peewee import AutoField, TextField, TimestampField

from hooply.market.models.base import BaseModel


class Game(BaseModel):
    id = AutoField()
    name = TextField()
    date = TimestampField()
    home_team = TextField()
    away_team = TextField()
