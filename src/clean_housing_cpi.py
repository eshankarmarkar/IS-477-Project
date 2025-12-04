import json
from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/clean")
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

def clean_housing():
    raw_path = RAW_DIR / "housing_fred.json"
    out_path = CLEAN_DIR / "housing_clean.csv"
    with raw_path.open() as f:
        data = json.load(f)
    obs = data["observations"]
    df = pd.DataFrame(obs)
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    housing_yearly = df.groupby("year", as_index=False)["value"].mean()
    housing_yearly = housing_yearly.rename(columns={"value": "avg_sales_price"})
    housing_yearly.to_csv(out_path, index=False)

def clean_cpi():
    raw_path = RAW_DIR / "cpi_fred.json"
    out_path = CLEAN_DIR / "cpi_clean.csv"
    with raw_path.open() as f:
        data = json.load(f)
    obs = data["observations"]
    df = pd.DataFrame(obs)
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    cpi_yearly = df.groupby("year", as_index=False)["value"].mean().rename(columns={"value": "cpi"})
    cpi_yearly.to_csv(out_path, index=False)

if __name__ == "__main__":
    clean_housing()
    clean_cpi()
