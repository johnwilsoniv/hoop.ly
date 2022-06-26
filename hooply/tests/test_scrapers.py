from hooply.market.scrapers.scraper import Scraper, RequestResources, DEFAULT_REQUEST_HEADERS, DEFAULT_REQUEST_TIMEOUT
from pytest import raises


def test_scraper_initialization():
    s = Scraper(RequestResources.BOXSCORES.value)

    assert s.params == {}
    assert s.headers == DEFAULT_REQUEST_HEADERS
    assert s.timeout == DEFAULT_REQUEST_TIMEOUT


def test_scraper_scrape_not_implemented():
    s = Scraper(RequestResources.BOXSCORES.value)

    with raises(NotImplementedError):
        s.scrape()
