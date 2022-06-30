from peewee import AutoField, DecimalField, IntegerField, TextField, ForeignKeyField

from hooply.market.models.base import BaseModel
from hooply.market.models.team import Team


class GameTeamBoxscore(BaseModel):
    id = AutoField()
    team_id = ForeignKeyField(Team, backref='team')
    pace = DecimalField()
    pts = DecimalField()
    opp_pts = DecimalField()
    efg = DecimalField()
    ortg = DecimalField()
    drtg = DecimalField()