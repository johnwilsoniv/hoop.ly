from peewee import AutoField, DecimalField, IntegerField, TextField

from hooply.market.models.base import BaseModel


class GameTeamBoxscore(BaseModel):
    id = AutoField()
    # Replace with backref key
    # game_id = IntegerField()
    team = TextField()
    pace = DecimalField()
    efg = DecimalField()
    ortg = DecimalField()
