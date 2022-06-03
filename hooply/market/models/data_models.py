class Player:
    def __init__(self, name, player_id, team_id):
        self.name = name
        self.player_id = player_id
        self.team_id = team_id


class BoxScoreRecord:
    def __init__(self, game_id, team_id, player_id, min, fgm, fga, fg3m, fg3a, ftm, fta, oreb, dreb, reb, ast, stl, blk, to, pts, pf, plus_minus):
        self.game_id = game_id
        self.team_id = team_id
        self.player_id = player_id
        self.min = min
        self.fgm = fgm
        self.fga = fga
        self.fg3m = fg3m
        self.fg3a = fg3a
        self.ftm = ftm
        self.fta = fta
        self.oreb = oreb
        self.dreb = dreb
        self.reb = reb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.to = to
        self.pts = pts
        self.pf = pf
        self.plus_minus = plus_minus
#
# class Game:
#     def __init__(self, season_id, game_id, home_team_id, away_team_id, ):