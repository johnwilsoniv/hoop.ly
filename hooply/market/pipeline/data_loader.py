from typing import Dict

from peewee import Database, DatabaseError

from hooply.logger import setup_logger
from hooply.market.models.game import Game
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.game_team import GameTeamBoxscore
from hooply.market.models.meta_ingestion import MetaIngestion
from hooply.market.models.player import Player
from hooply.market.models.team import Team
from hooply.market.scrapers.scraper import ScrapeResult, ScrapeResultType

DEFAULT_SLEEP_TIMEOUT = 5
logger = setup_logger(__name__)


class DataLoader:
    @staticmethod
    def load_bipm(game: Game, db: Database):
        pass


    @staticmethod
    def load_teams(team_abbreviations: Dict[str, str], db: Database):
        with db.atomic() as txn:
            try:
                for abbreviation, name in team_abbreviations.items():
                    t = Team.create(abbreviation=abbreviation, name=name)
                    logger.info("Created team record (%s)", t)
            except DatabaseError:
                txn.rollback()

    @staticmethod
    def load_game(
        game_sr: ScrapeResult,
        team_sr: ScrapeResult,
        player_sr: ScrapeResult,
        db: Database,
    ) -> Game:
        if (
            team_sr.result_type != ScrapeResultType.teams_boxscore
            or player_sr.result_type != ScrapeResultType.players_boxscore
        ):
            exit(1)

        # Load game specific boxscore
        home_team_info, away_team_info = game_sr.data
        home_team_name, home_team_pts, _ = home_team_info
        away_team_name, away_team_pts, _ = away_team_info
        home_team_id, away_team_id = (
            Team.select(Team.id).where(Team.name == home_team_name).get(),
            Team.select(Team.id).where(Team.name == away_team_name).get(),
        )
        game = None

        with db.atomic() as txn:
            try:
                game = Game.create(
                    home_team_id=home_team_id, away_team_id=away_team_id
                )
                logger.info("Created game record (%s)", game)
            except DatabaseError:
                txn.rollback()

        # Load team specific boxscore
        with db.atomic() as txn:
            try:
                for team in team_sr.data:
                    team_record = (
                        Team.select().where(Team.abbreviation == team).get()
                    )
                    home_team_record = game.home_team

                    if team_record.id == home_team_record.id:
                        pts = home_team_pts
                        opp_pts = away_team_pts
                    else:
                        pts = away_team_pts
                        opp_pts = home_team_pts

                    pace, efg, ortg = team_sr.data[team]
                    drtg = round((float(opp_pts) / float(pace)), 2) * 100
                    gbs = GameTeamBoxscore.create(
                        team_id=team_record.id,
                        pace=pace,
                        efg=efg,
                        ortg=ortg,
                        drtg=drtg,
                        pts=pts,
                        opp_pts=opp_pts,
                        game_id=game.id,
                    )
                    logger.info("Created game boxscore record (%s)", gbs)
            except DatabaseError:
                txn.rollback()

        # Load player specific boxscore
        with db.atomic() as txn:
            try:
                for team_abbreviation in player_sr.data:
                    team = (
                        Team.select()
                        .where(Team.abbreviation == team_abbreviation)
                        .get()
                    )
                    for player_bs in player_sr.data[team_abbreviation]:
                        (
                            name,
                            mp,
                            fg,
                            fga,
                            tpg,
                            tpa,
                            ft,
                            fta,
                            orb,
                            drb,
                            _,
                            ast,
                            stl,
                            blk,
                            tov,
                            pf,
                            pts,
                            pm,
                        ) = player_bs
                        p = Player.select().where(Player.name == name).get()

                        if p is None:
                            # Player doesn't exist case
                            exit(1)

                        pbs = GamePlayerBoxscore.create(
                            player_id=p.id,
                            game_id=game.id,
                            team_id=team.id,
                            mp=mp,
                            fg=fg,
                            fga=fga,
                            tpg=tpg,
                            tpa=tpa,
                            ft=ft,
                            fta=fta,
                            orb=orb,
                            drb=drb,
                            ast=ast,
                            stl=stl,
                            blk=blk,
                            tov=tov,
                            pf=pf,
                            pts=pts,
                            pm=pm,
                        )
                        logger.info("Created player boxscore record (%s)", pbs)
            except DatabaseError:
                txn.rollback()

        # with db.atomic() as txn:
        #     try:
        #         m = MetaIngestion.create(type="player_boxscore")
        #         logger.info("Created meta ingestion record (%s)", m)
        #         txn.commit()
        #     except DatabaseError:
        #         txn.rollback()

        return game

    @staticmethod
    def load_team_roster(s: ScrapeResult, db: Database) -> None:
        if s.result_type != ScrapeResultType.player:
            logger.error("Replace.")
            exit(1)

        # Load player specific data
        with db.atomic() as txn:
            try:
                for player in s.data:
                    name, _, position, height, weight = player
                    p = Player.create(
                        name=name,
                        position=position,
                        height=height,
                        weight=weight,
                    )
                    logger.info("Created player (%s)", p)
                txn.commit()
            except DatabaseError:
                txn.rollback()

        # with db.atomic() as txn:
        #     try:
        #         m = MetaIngestion.create(type="player")
        #         logger.info("Created meta ingestion record (%s)", m)
        #         txn.commit()
        #     except DatabaseError:
        #         txn.rollback()

    @staticmethod
    def _load_bipm(s: ScrapeResult) -> None:
        raise NotImplementedError
