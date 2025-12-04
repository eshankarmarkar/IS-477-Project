from pathlib import Path
import requests

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

FRED_API_KEY = "18d62bb20c7238fec4b5145abcbb9af7"
FRED_BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

def download_fred_series(series_id, dest, observation_start):
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": observation_start,
    }
    r = requests.get(FRED_BASE_URL, params=params)
    r.raise_for_status()
    dest.write_text(r.text)

def get_housing():
    download_fred_series("ASPUS", RAW_DIR / "housing_fred.json", "1963-01-01")

def get_cpi():
    download_fred_series("CPIAUCSL", RAW_DIR / "cpi_fred.json", "1960-01-01")

if __name__ == "__main__":
    get_housing()
    get_cpi()
