from enum import Enum

# Scraper variables
DEFAULT_REQUEST_HEADERS = {}
DEFAULT_REQUEST_TIMEOUT = 100
DEFAULT_HOST = "https://www.basketball-reference.com"
# Pipeline variables
DEFAULT_QUEUE_NAME = "daily-ingestion-queue"

DEV_SEASON = "2017"
DEV_SEASON_START = "2016-12-25"
DEV_SEASON_END = "2016-12-25"

DEV_TEAM_ABBREVIATIONS = {
    # "BOS": "Boston Celtics",
    "CLE": "Cleveland Cavaliers",
    "GSW": "Golden State Warriors",
}


PROD_TEAM_ABBREVIATIONS = {
    "MIA": "Miami Heat",
    "BOS": "Boston Celtics",
    "MIL": "Milwaukee Bucks",
    "PHI": "Philadelphia 76ers",
    "TOR": "Toronto Raptors",
    "CHI": "Chicago Bulls",
    "BRK": "Brooklyn Nets",
    "CLE": "Cleveland Cavaliers",
    "ATL": "Atlanta Hawks",
    "CHO": "Charlotte Hornets",
    "NYK": "New York Knicks",
    "WAS": "Washington Wizards",
    "IND": "Indiana Pacers",
    "DET": "Detroit Pistons",
    "ORL": "Orlando Magic",
    "PHO": "Phoenix Suns",
    "MEM": "Memphis Grizzlies",
    "GSW": "Golden State Warriors",
    "DAL": "Dallas Mavericks",
    "UTA": "Utah Jazz",
    "DEN": "Denver Nuggets",
    "MIN": "Minnesota Timberwolves",
    "LAC": "Los Angeles Clippers",
    "NOP": "New Orleans Pelicans",
    "LAL": "Los Angeles Lakers",
    "SAS": "San Antonio Spurs",
    "POR": "Portland Trail Blazers",
    "OKC": "Oklahoma City Thunder",
    "HOU": "Houston Rockets",
}

PROD_SEASON = "2022"
PROD_SEASON_START = "2022-06-16"