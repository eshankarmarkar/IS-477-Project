from pathlib import Path
import pandas as pd

CLEAN_DIR = Path("data/clean")
OUT_PATH = CLEAN_DIR / "merged_affordability.csv"

def main():
    income = pd.read_csv(CLEAN_DIR / "income_clean.csv")
    housing = pd.read_csv(CLEAN_DIR / "housing_clean.csv")
    cpi = pd.read_csv(CLEAN_DIR / "cpi_clean.csv")
    base_year = cpi["year"].max()
    base_cpi = cpi.loc[cpi["year"] == base_year, "cpi"].iloc[0]
    cpi["inflation_factor_to_base"] = base_cpi / cpi["cpi"]
    merged = housing.merge(income, on="year", how="inner")
    merged = merged.merge(cpi[["year", "inflation_factor_to_base"]], on="year", how="left")
    merged["median_income_real"] = merged["median_income_nominal"] * merged["inflation_factor_to_base"]
    merged["avg_sales_price_real"] = merged["avg_sales_price"] * merged["inflation_factor_to_base"]
    merged = merged.sort_values("year")
    merged["afford_ratio_nominal"] = merged["avg_sales_price"] / merged["median_income_nominal"]
    merged["afford_ratio_real"] = merged["avg_sales_price_real"] / merged["median_income_real"]
    merged["pct_change_income_real"] = merged["median_income_real"].pct_change(fill_method=None) * 100
    merged["pct_change_housing_real"] = merged["avg_sales_price_real"].pct_change(fill_method=None) * 100
    merged["growth_gap_pp"] = merged["pct_change_housing_real"] - merged["pct_change_income_real"]
    merged.to_csv(OUT_PATH, index=False)

if __name__ == "__main__":
    main()
