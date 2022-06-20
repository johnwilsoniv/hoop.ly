from hooply.market.scrapers.scraper import Scraper, Resources, DEFAULT_REQUEST_HEADERS, DEFAULT_REQUEST_TIMEOUT
from pytest import raises


def test_scraper_initialization():
    s = Scraper(Resources.BOXSCORES.value)

    assert s.params == {}
    assert s.headers == DEFAULT_REQUEST_HEADERS
    assert s.timeout == DEFAULT_REQUEST_TIMEOUT


def test_scraper_scrape_not_implemented():
    s = Scraper(Resources.BOXSCORES.value)

    with raises(NotImplementedError):
        s.scrape()
