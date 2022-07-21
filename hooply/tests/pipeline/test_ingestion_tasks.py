from hooply.market.pipeline.ingestion_tasks import IngestionTask, IngestTeamsTask, IngestGameTask
from hooply.market.scrapers.scraper import ScrapeResult, ScrapeResultType
from unittest.mock import MagicMock, Mock, patch
from peewee import Database, SqliteDatabase
from pandas import Timestamp


MOCK_DB = Database(Mock())
MOCK_DATE = Timestamp('2021-07-01')
MOCK_TEAMS = {
    't1': 'team 1',
    't2': 'team 2',
}
MOCK_SEASON = '2022'


def test_ingestion_tasks_subclass():
    assert issubclass(IngestTeamsTask, IngestionTask) is True
    assert issubclass(IngestGameTask, IngestionTask) is True


@patch('hooply.market.pipeline.ingestion_tasks.TeamRosterScraper')
@patch('hooply.market.pipeline.ingestion_tasks.DataLoader')
def test_ingestion_teams_task(mock_loader, mock_tr_scraper_cls):
    mock_teams_task = IngestTeamsTask(MOCK_TEAMS, MOCK_SEASON, MOCK_DB)
    mock_scraper = Mock(name="scraper")
    mock_sr = ScrapeResult(ScrapeResultType.player, [])
    mock_scraper.scrape.return_value = [mock_sr]

    mock_tr_scraper_cls.generate_resource.return_value = None
    mock_tr_scraper_cls.return_value = mock_scraper


    assert mock_teams_task.run() == None


@patch('hooply.market.pipeline.ingestion_tasks.DateScraper')
@patch('hooply.market.pipeline.ingestion_tasks.GameScraper')
@patch('hooply.market.pipeline.ingestion_tasks.DataLoader')
def test_ingestion_game_task(mock_loader, mock_g_scraper_cls, mock_d_scraper_cls):
    mock_game_task = IngestGameTask(MOCK_DATE, MOCK_DB)
    TEST_GAME = "202206160BOS.html"

    mock_g_scraper = Mock(name="g scraper")
    mock_d_scraper = Mock(name="d scraper")

    mock_d_scraper.scrape.return_value = [ScrapeResult(ScrapeResultType.multiple_games_link, [TEST_GAME])]
    mock_g_scraper.scrape.return_value = [ScrapeResult(ScrapeResultType.game, []), ScrapeResult(ScrapeResultType.teams_boxscore, []), ScrapeResult(ScrapeResultType.players_boxscore, [])]

    mock_g_scraper_cls.return_value = mock_g_scraper
    mock_d_scraper_cls.return_value = mock_d_scraper


    assert mock_game_task.run() == None
