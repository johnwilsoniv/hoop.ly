from peewee import AutoField, DecimalField, ForeignKeyField, IntegerField, TextField

from hooply.market.models.base import BaseModel
from hooply.market.models.game import Game
from hooply.market.models.team import Team


class GameTeamBoxscore(BaseModel):
    id = AutoField()
    team_id = ForeignKeyField(Team, backref="team")
    game_id = ForeignKeyField(Game, backref="game")
    pace = DecimalField()
    pts = DecimalField()
    opp_pts = DecimalField()
    efg = DecimalField()
    ortg = DecimalField()
    drtg = DecimalField()
