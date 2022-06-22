from enum import Enum

DEFAULT_REQUEST_HEADERS = {}
DEFAULT_REQUEST_TIMEOUT = 1
DEFAULT_HOST = "https://www.basketball-reference.com"
DEFAULT_QUEUE_NAME = "daily-ingestion-queue"


class Resources(Enum):
    BOXSCORES = "boxscores"
    PLAYERS = "players"


DEFAULT_SEASON = "2022"
TEAM_ABBREVIATIONS = [
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
