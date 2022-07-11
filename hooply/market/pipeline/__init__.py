from enum import Enum

# Scraper variables
DEFAULT_REQUEST_HEADERS = {}
DEFAULT_REQUEST_TIMEOUT = 1
DEFAULT_HOST = "https://www.basketball-reference.com"
# Pipeline variables
DEFAULT_QUEUE_NAME = "daily-ingestion-queue"

DEV_SEASON = "2022"
DEV_SEASON_START = "2022-06-02"
DEV_SEASON_END = "2022-06-16"

DEV_TEAM_ABBREVIATIONS = {
    "BOS": "Boston Celtics",
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
