from typing import List, Protocol
from dataclasses import dataclass
from bs4 import BeautifulSoup
from requests import Session
from requests.exceptions import RequestException
from hooply.logger import setup_logger
from hooply.market.pipeline import DEFAULT_HOST, DEFAULT_REQUEST_HEADERS, DEFAULT_REQUEST_TIMEOUT
from os import path

logger = setup_logger(__name__)


@dataclass
class ScrapeResult:
    resource: str
    data: List[List[str]]


class Scraper(Protocol):
    def __init__(self, resource, params=None, headers=None, timeout=None):
        if params is None:
            params = dict()
        if headers is None:
            headers = DEFAULT_REQUEST_HEADERS
        if timeout is None:
            timeout = DEFAULT_REQUEST_TIMEOUT

        self.url = path.join(DEFAULT_HOST, resource)
        self.params = params
        self.headers = headers
        self.timeout = timeout

    def scrape(self) -> ScrapeResult:
        ...

    def request(self) -> BeautifulSoup:
        try:
            logger.info(
                "Requesting resource: (%s), (%s), (%s).",
                self.url,
                self.params,
                self.headers,
            )
            s = Session()
            resp = s.get(
                url=self.url,
                params=self.params,
                timeout=self.timeout,
                headers=self.headers,
            )
        except RequestException as e:
            logger.error(e)
            exit(1)

        html = "".join(line.strip() for line in resp.text.split("\n"))
        return BeautifulSoup(html, "html.parser")
