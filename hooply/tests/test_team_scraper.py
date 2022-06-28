from typing import List, Dict, Tuple
from hooply.market.scrapers.scraper import (
    RequestResources,
    ScrapeResult,
    ScrapeResultType,
)
from hooply.market.scrapers.team_scraper import TeamRosterScraper
from unittest.mock import Mock, patch, MagicMock
from pytest import raises

TEST_TEAM = "BOS"
TEST_SEASON = "2022"


def test_team_scraper_generate():
    assert (
        TeamRosterScraper.generate_resource(TEST_TEAM, TEST_SEASON)
        == f"teams/{TEST_TEAM}/{TEST_SEASON}.html"
    )


@patch.object(TeamRosterScraper, "request")
def test_team_scraper_scrape_roster_div_not_found(patched_request: MagicMock):
    mock_soup = Mock(name="soup")
    patched_request.return_value = mock_soup

    mock_soup.find.return_value = None

    resource = TeamRosterScraper.generate_resource(TEST_TEAM, TEST_SEASON)
    test_trs = TeamRosterScraper(resource=resource)

    with raises(SystemExit):
        test_trs.scrape()


@patch.object(TeamRosterScraper, "request")
def test_team_scraper_scrape_no_players_found(patched_request: MagicMock):
    mock_soup, mock_roster_div = Mock(name="soup"), Mock(name="roster_div")
    patched_request.return_value = mock_soup

    mock_soup.find.return_value = mock_roster_div
    mock_roster_div.find.return_value.children = iter([])

    resource = TeamRosterScraper.generate_resource(TEST_TEAM, TEST_SEASON)
    test_trs = TeamRosterScraper(resource=resource)

    assert test_trs.scrape() == [
        ScrapeResult(result_type=ScrapeResultType.player, data=[])
    ]


@patch.object(TeamRosterScraper, "_extract_player")
@patch.object(TeamRosterScraper, "request")
def test_team_scraper_scrape_player_found(
    patched_request: MagicMock, patched_extract_player: MagicMock
):
    mock_soup, mock_roster_div = Mock(name="soup"), Mock(name="roster_div")
    patched_request.return_value = mock_soup

    # Setup mocks to avoid bs4 parsing method
    players = [
        ["Jaylen Brown", "SF", "6-6", "223"],
        ["Jayson Tatum", "SF", "6-8", "210"],
    ]
    player_mocks = [Mock(children=player) for player in players]

    mock_soup.find.return_value = mock_roster_div
    mock_roster_div.find.return_value.children = player_mocks
    patched_extract_player.side_effect = players

    resource = TeamRosterScraper.generate_resource(TEST_TEAM, TEST_SEASON)
    test_trs = TeamRosterScraper(resource=resource)

    assert test_trs.scrape() == [
        ScrapeResult(result_type=ScrapeResultType.player, data=players)
    ]
