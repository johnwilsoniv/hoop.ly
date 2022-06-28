from typing import List, Dict, Tuple
from hooply.market.scrapers.scraper import RequestResources, ScrapeResult, ScrapeResultType
from hooply.market.scrapers.game_scraper import GameScraper
from unittest.mock import Mock, patch, MagicMock
from pytest import raises

TEST_GAME = '202206160BOS.html'


def test_game_scraper_generate():
    assert GameScraper.generate_resource(TEST_GAME) == f'boxscores/{TEST_GAME}'


@patch.object(GameScraper, '_extract_player_factors')
@patch.object(GameScraper, '_extract_four_factors')
@patch.object(GameScraper, '_extract_game')
@patch.object(GameScraper, 'request')
def test_game_scraper(patched_request: MagicMock, patched_extract_game: MagicMock, patched_extract_four_factors: MagicMock, patched_extract_player_factors: MagicMock):
    mock_soup = Mock(name="soup")
    patched_request.return_value = mock_soup

    # Setup mocks to avoid bs4 parsing method
    mock_soup.find.return_value = None
    test_team_four_factors = {'GSW': ['92.1', '.516', '111.8'], 'BOS': ['92.1', '.494', '97.7']}
    test_game_info = [['Boston Celtics', '90', '2-4'], ['Golden State Warriors', '103', '4-2']]
    test_players = {'GSW': ['Andrew Wiggins', '43:41', '7', '18', '4', '9', '0', '0', '3', '3', '6', '5', '4', '3', '3', '0', '18', '+5'], 'BOS': ['Jaylen Brown', '44:00', '12', '23', '5', '11', '5', '6', '1', '6', '7', '3', '1', '0', '5', '2', '34', '+1']}

    patched_extract_game.return_value = test_game_info
    patched_extract_four_factors.return_value = test_team_four_factors
    patched_extract_player_factors.return_value = test_players

    resource = GameScraper.generate_resource(TEST_GAME)
    test_gs = GameScraper(resource=resource)

    assert test_gs.scrape() == [
        ScrapeResult(ScrapeResultType.game, test_game_info),
        ScrapeResult(ScrapeResultType.teams_boxscore, test_team_four_factors),
        ScrapeResult(ScrapeResultType.players_boxscore, test_players)
    ]

