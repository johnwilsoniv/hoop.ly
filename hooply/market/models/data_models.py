from peewee import *

db = MySQLDatabase(
    database="hooply",
    host="localhost",
    port=3306,
    user="root",
    password="test",
    # pragmas={"journal_mode": "wal", "cache_size": 10000, "foreign_keys": 1},
)


class Player(Model):
    name = TextField()
    player_id = IntegerField(primary_key=True)
    team_id = IntegerField()

    class Meta:
        database = db
        db_table = "players"

    def __str__(self):
        return self.name


# class BoxScoreRecord:
#     def __init__(self, game_id, team_id, player_id, min, fgm, fga, fg3m, fg3a, ftm, fta, oreb, dreb, reb, ast, stl, blk, to, pts, pf, plus_minus):
#         # self.game_id = game_id
#         # self.team_id = team_id
#         # self.player_id = player_id
#         # self.min = min
#         # self.fgm = fgm
#         # self.fga = fga
#         # self.fg3m = fg3m
#         # self.fg3a = fg3a
#         # self.ftm = ftm
#         # self.fta = fta
#         # self.oreb = oreb
#         # self.dreb = dreb
#         # self.reb = reb
#         # self.ast = ast
#         # self.stl = stl
#         # self.blk = blk
#         # self.to = to
#         # self.pts = pts
#         # self.pf = pf
#         # self.plus_minus = plus_minus
# #
# class Game:
#     def __init__(self, season_id, game_id, home_team_id, away_team_id, game):
if __name__ == "__main__":
    db.connect()
    db.create_tables([Player])
