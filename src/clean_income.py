import pandas as pd
import re
from pathlib import Path

RAW_PATH = Path("data/raw/incomedata.csv")
OUT_PATH = Path("data/clean/income_clean.csv")
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

def main():
    raw = pd.read_csv(RAW_PATH, header=None)
    header_top = raw.iloc[2]
    header_bottom = raw.iloc[3]
    combined_cols = []
    for top, bottom in zip(header_top, header_bottom):
        top = "" if pd.isna(top) else str(top).strip()
        bottom = "" if pd.isna(bottom) else str(bottom).strip()
        if top and bottom:
            combined_cols.append(f"{top} {bottom}")
        elif top:
            combined_cols.append(top)
        else:
            combined_cols.append(bottom)
    all_races_mask = raw[0].astype(str).str.strip().eq("ALL RACES")
    if not all_races_mask.any():
        raise ValueError("Couldn't find 'ALL RACES' in column 0.")
    start_idx = raw[all_races_mask].index[0] + 1
    rows = []
    for i in range(start_idx, len(raw)):
        val = str(raw.iloc[i, 0]).strip()
        if val in ["White", "Black", "Asian", "Hispanic origin (any race)", "Hispanic origin"]:
            break
        if re.search(r"\d{4}", val):
            rows.append(i)
    data = raw.iloc[rows].copy()
    data.columns = combined_cols
    year_col = next((c for c in data.columns if "Origin of householder" in c or "year" in c.lower()), None)
    income_col = next((c for c in data.columns if "Median income" in c and "dollars" in c), None)
    if not year_col or not income_col:
        raise ValueError(f"Couldn't detect columns. year_col={year_col}, income_col={income_col}")
    df = data[[year_col, income_col]].rename(columns={year_col: "year", income_col: "median_income_nominal"})
    df["year"] = df["year"].astype(str).str.extract(r"(\d{4})")
    df = df[df["year"].notna()]
    df["year"] = df["year"].astype(int)
    df["median_income_nominal"] = df["median_income_nominal"].astype(str).str.replace(",", "", regex=False).astype(float)
    df = df.sort_values("year").reset_index(drop=True)
    df.to_csv(OUT_PATH, index=False)

if __name__ == "__main__":
    main()
