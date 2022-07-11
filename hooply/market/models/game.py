from peewee import AutoField, ForeignKeyField, TextField, TimestampField

from hooply.market.models.base import BaseModel
from hooply.market.models.team import Team


class Game(BaseModel):
    id = AutoField()
    home_team_id = ForeignKeyField(Team, backref="team")
    away_team = ForeignKeyField(Team, backref="team")
    date = TimestampField()
