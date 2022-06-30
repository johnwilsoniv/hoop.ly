from peewee import AutoField, TextField, TimestampField

from hooply.market.models.base import BaseModel


class Team(BaseModel):
    id = AutoField()
    abbreviation = TextField()
    name = TextField()
