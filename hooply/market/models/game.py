from hooply.market.models.base import BaseModel
from peewee import AutoField, TextField, TimestampField


class Game(BaseModel):
    id = AutoField()
    name = TextField()
    date = TimestampField()
    home_team = TextField()
    away_team = TextField()
