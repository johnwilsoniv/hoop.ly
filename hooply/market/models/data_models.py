from peewee import *
from hooply.market import db


class Player(Model):
    name = TextField()
    player_id = IntegerField(primary_key=True)
    team_id = IntegerField()

    class Meta:
        database = db
        db_table = "players"


class Game(Model):
    game_id = IntegerField(primary_key=True)
    home_team_id = IntegerField()
    away_team_id = IntegerField()
    home_team_name = TextField()
    away_team_name = TextField()
    date = TextField()
    matchup = TextField()

    class Meta:
        database = db
        db_table = "game"


class BoxScoreRecord(Model):
    team_id = IntegerField()
    player_id = IntegerField()
    min = TextField()
    fgm = IntegerField()
    fga = IntegerField()
    fg3m = IntegerField()
    fg3a = IntegerField()
    ftm = IntegerField()
    fta = IntegerField()
    oreb = IntegerField()
    dreb = IntegerField()
    reb = IntegerField()
    ast = IntegerField()
    stl = IntegerField()
    blk = IntegerField()
    to = IntegerField()
    pts = IntegerField()
    pf = IntegerField()
    plus_minus = IntegerField()

    class Meta:
        database = db
        db_table = "boxscorerecord"


class StockPrice(Model):
    player_id = IntegerField()
    date = TextField()
    price = DecimalField()
    method = TextField()

    class Meta:
        database = db
        db_table = "stockprice"


if __name__ == '__main__':
    db.connect()
    db.create_tables([Player, Game, BoxScoreRecord, StockPrice])
