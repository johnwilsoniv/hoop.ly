from enum import Enum

# Scraper variables
DEFAULT_REQUEST_HEADERS = {}
DEFAULT_REQUEST_TIMEOUT = 1
DEFAULT_HOST = "https://www.basketball-reference.com"
# Pipeline variables
DEFAULT_QUEUE_NAME = "daily-ingestion-queue"

DEV_SEASON = "2022"
DEV_SEASON_START = "2021-06-15"
DEV_SEASON_END = "2022-06-15"

DEV_TEAM_ABBREVIATIONS = [
    "BOS",
    "GSW"
]
PROD_TEAM_ABBREVIATIONS = [
    "MIA",
    "BOS",
    "MIL",
    "PHI",
    "TOR",
    "CHI",
    "BRK",
    "CLE",
    "ATL",
    "CHO",
    "NYK",
    "WAS",
    "IND",
    "DET",
    "ORL",
    "PHO",
    "MEM",
    "GSW",
    "DAL",
    "UTA",
    "DEN",
    "MIN",
    "LAC",
    "NOP",
    "SAS",
    "LAL",
    "SAS",
    "POR",
    "OKC",
    "HOU"
]
