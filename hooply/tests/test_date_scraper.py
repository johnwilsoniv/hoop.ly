from typing import List, Dict, Tuple
from hooply.market.scrapers.scraper import RequestResources, ScrapeResult, ScrapeResultType
from hooply.market.scrapers.date_scraper import DateScraper, Scraper
from pandas import Timestamp
from unittest.mock import Mock, patch, MagicMock

TEST_DATE = ["2022", "7", "1"]


def setup_date_scraper_reqs(test_date: List[str]) -> Tuple[str, Dict]:
    test_ts = Timestamp("-".join(test_date))

    params = DateScraper.generate_params(test_ts)
    resource = DateScraper.generate_resource()
    return resource, params


def test_date_scraper_generate():
    resource, params = setup_date_scraper_reqs(TEST_DATE)

    assert params == {
        "month": TEST_DATE[1],
        "day": TEST_DATE[2],
        "year": TEST_DATE[0]
    }
    assert resource == RequestResources.BOXSCORES.value


@patch.object(DateScraper, 'request')
def test_date_scraper_scrape_no_games_found(patched_request: MagicMock):
    mock_soup = Mock(name="soup")
    patched_request.return_value = mock_soup

    mock_soup.find_all.return_value = []

    resource, params = setup_date_scraper_reqs(TEST_DATE)
    test_ds = DateScraper(resource=resource, params=params)

    assert test_ds.scrape() == [ScrapeResult(result_type=ScrapeResultType.multiple_games_link, data=[])]


@patch.object(DateScraper, '_extract_game')
@patch.object(DateScraper, 'request')
def test_date_scraper_scrape_multiple_games_found(patched_request: MagicMock, patched_extract_game: MagicMock):
    mock_soup = Mock(name="soup")
    mock_games = [Mock(), Mock()]
    mock_soup.find_all.return_value = mock_games
    game_links = ['202207010BOS.html','202207011GSW.html']

    patched_request.return_value = mock_soup
    patched_extract_game.side_effect = game_links
    resource, params = setup_date_scraper_reqs(TEST_DATE)
    test_ds = DateScraper(resource=resource, params=params)

    expected = ScrapeResult(result_type=ScrapeResultType.multiple_games_link, data=game_links)
    res = test_ds.scrape()[0]

    assert res.data == expected.data and res.result_type == expected.result_type


