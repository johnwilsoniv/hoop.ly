from peewee import Database, DatabaseError
from hooply.logger import setup_logger
from hooply.market.scrapers.scraper import ScrapeResult, ScrapeResultType
from hooply.market.models.player import Player
from hooply.market.models.game_player import GamePlayerBoxscore
from hooply.market.models.meta_ingestion import MetaIngestion

DEFAULT_SLEEP_TIMEOUT = 5
logger = setup_logger(__name__)


# def load_players():
#     pass
#
# def ingest_player_data():
#     pass

class DataLoader:

    @staticmethod
    def load_game(team_sr: ScrapeResult, player_sr: ScrapeResult, db: Database) -> None:
        if team_sr.result_type != ScrapeResultType.teams_boxscore or player_sr.result_type != ScrapeResultType.players_boxscore:
            logger.error("Replace.")
            exit(1)

        with db.atomic() as txn:
            try:
                for team in player_sr.data:
                    for player_bs in player_sr.data[team]:
                        name, mp, fg, fga, tpg, tpa, ft, fta, orb, drb, _, ast, stl, blk, tov, pf, pts, pm = player_bs
                        pbs = GamePlayerBoxscore.create(player=name, team=team, mp=min, fg=fg, fga=fga, tpg=tpg, tpa=tpa,
                                                 ft=ft, fta=fta, orb=orb, drb=drb, ast=ast, stl=stl, blk=blk, tov=tov,
                                                 pf=pf, pts=pts, pm=pm)
                        logger.info("Created player boxscore record (%s)", pbs)
            except DatabaseError:
                txn.rollback()

        with db.atomic() as txn:
            try:
                m = MetaIngestion.create(type="player_boxscore")
                logger.info("Created meta ingestion record (%s)", m)
                txn.commit()
            except DatabaseError:
                txn.rollback()

    @staticmethod
    def load_team_roster(s: ScrapeResult, db: Database) -> None:
        if s.result_type != ScrapeResultType.player:
            logger.error("Replace.")
            exit(1)

        with db.atomic() as txn:
            try:
                for player in s.data:
                    name, _, position, height, weight = player
                    p = Player.create(name=name, position=position, height=height, weight=weight)
                    logger.info("Created player (%s)", p)
                txn.commit()
            except DatabaseError:
                txn.rollback()

        with db.atomic() as txn:
            try:
                m = MetaIngestion.create(type="player")
                logger.info("Created meta ingestion record (%s)", m)
                txn.commit()
            except DatabaseError:
                txn.rollback()

    @staticmethod
    def _load_bipm(s: ScrapeResult) -> None:
        raise NotImplementedError




# def _load_game():
#     with db.atomic() as game_txn:
#         # do stuff
#         pass
#
#         with db.atomic() as boxscore_txn:
#             pass


# def load_date_boxscore(d: date) -> None:
#     year, month, day = d.isoformat().split("-")
#     params = {
#         "month": month,
#         "day": day,
#         "year": year
#     }
#     ds = DateScraper(resource=Resources.BOXSCORES.value, params=params)
#     game_links = ds.scrape()
#
#     if not game_links:
#         logger.info("No data ingested for date: (%s).", d)
#         return
#
#     for gl in game_links[0:1]:
#         s = GameScraper(path.join(Resources.BOXSCORES.value, gl))
#         game_information, team_boxscore, player_boxscore = s.scrape()
#         # _load_game()
#         sleep(DEFAULT_SLEEP_TIMEOUT)

        # # load_player_boxscore(player_boxscore)
        # load_team_boxscore(team_boxscore)

    # gl = "202110200CHO.html"
    # s = GameScraper(path.join(Resources.BOXSCORES.value, gl))
    # s.scrape()

    # s = DateScraper(params={
    #     "month": "10",
    #     "day": "20",
    #     "year": "2021"
    # })

    # Generate all dates between start and end
    # For each -> Date Scrape, if games -> generate all Game Scraper params -> Game Scrape -> save


# def load_teams() -> None:
#     pass
#
#
# def load_players() -> None:
#     pass
