from hooply.market.models.base import BaseModel
from peewee import AutoField, TextField, IntegerField, DecimalField


class GameTeamBoxscore(BaseModel):
    id = AutoField()
    # Replace with backref key
    # game_id = IntegerField()
    team = TextField()
    pace = DecimalField()
    efg = DecimalField()
    ortg = DecimalField()

