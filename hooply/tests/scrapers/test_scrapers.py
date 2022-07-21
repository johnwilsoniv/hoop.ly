from unittest.mock import Mock, patch

from pytest import raises
from requests import RequestException, Response, Session

from hooply.market.scrapers.scraper import (
    DEFAULT_REQUEST_HEADERS,
    DEFAULT_REQUEST_TIMEOUT,
    RequestResources,
    Scraper,
)


def test_scraper_initialization():
    s = Scraper(RequestResources.BOXSCORES.value)

    assert s.params == {}
    assert s.headers == DEFAULT_REQUEST_HEADERS
    assert s.timeout == DEFAULT_REQUEST_TIMEOUT


def test_scraper_scrape_not_implemented():
    s = Scraper(RequestResources.BOXSCORES.value)

    with raises(NotImplementedError):
        s.scrape()


@patch.object(Session, "get")
def test_scraper_request_exception(patched_get):
    patched_get.side_effect = RequestException
    s = Scraper(RequestResources.BOXSCORES.value)

    with raises(SystemExit):
        s.request()


@patch.object(Session, "get")
def test_scraper_request_successful(patched_get):
    s = Scraper(RequestResources.BOXSCORES.value)

    patched_get.return_value = Response()
    s.request()
