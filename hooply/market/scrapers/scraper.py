from typing import Protocol
from bs4 import BeautifulSoup
from hooply.market.logger import setup_logger
import requests

logger = setup_logger(__name__)

class Scraper(Protocol):

    def scrape(self):
        pass


class DateScraper(Scraper):
    pass


class GameScraper(Scraper):
    pass


class PlayerScraper(Scraper):
    pass


if __name__ == '__main__':
    logger.info("Hello")
