from hooply.market.scrapers.scraper import (
    Scraper,
    RequestResources,
    DEFAULT_REQUEST_HEADERS,
    DEFAULT_REQUEST_TIMEOUT,
)
from requests import Session
from pytest import raises
from requests import Response, RequestException
from unittest.mock import Mock, patch


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
