from peewee import *
from hooply.market import db


class GameTeamBoxscore(Model):
    id = AutoField()
    # Replace with backref key
    game_id = IntegerField()
    pace = DecimalField()
    efg = DecimalField()
    ortg = DecimalField()

    class Meta:
        database = db
        table_name = "game_team_boxscore"
