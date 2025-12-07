from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PLOT_DIR = Path("output/plots")

if PLOT_DIR.parent.exists() and not PLOT_DIR.parent.is_dir():
    PLOT_DIR.parent.unlink()
if not PLOT_DIR.parent.exists():
    PLOT_DIR.parent.mkdir(parents=True, exist_ok=True)

if PLOT_DIR.exists() and not PLOT_DIR.is_dir():
    PLOT_DIR.unlink()
PLOT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/clean/merged_affordability.csv")
df = df.sort_values("year")

num_cols = [
    "median_income_real",
    "avg_sales_price_real",
    "afford_ratio_real",
    "pct_change_income_real",
    "pct_change_housing_real",
    "growth_gap_pp",
]
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=["median_income_real", "avg_sales_price_real", "afford_ratio_real"])

plt.figure(figsize=(8, 4.5))
plt.plot(df["year"], df["median_income_real"] / 1000, label="Median household income (real, $K)")
plt.plot(df["year"], df["avg_sales_price_real"] / 1000, label="Avg house price (real, $K)")
plt.title("Real Income vs Real House Prices (inflation-adjusted to latest CPI)")
plt.xlabel("Year")
plt.ylabel("Dollars (thousands)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(PLOT_DIR / "01_income_vs_price_real.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 4.5))
plt.plot(df["year"], df["afford_ratio_real"])
plt.title("Affordability Ratio (Real House Price ÷ Real Income)")
plt.xlabel("Year")
plt.ylabel("Ratio (higher = less affordable)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(PLOT_DIR / "02_affordability_ratio.png", dpi=300)
plt.close()

recent = df[df["year"] >= 2000].copy()
plt.figure(figsize=(8, 4.5))
plt.plot(recent["year"], recent["pct_change_housing_real"], label="Housing % change (real)")
plt.plot(recent["year"], recent["pct_change_income_real"], label="Income % change (real)")
plt.title("Year-over-Year Growth: Housing vs Income (Real, 2000+)")
plt.xlabel("Year")
plt.ylabel("% change from previous year")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(PLOT_DIR / "03_yoy_growth_recent.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 4.5))
plt.bar(recent["year"], recent["growth_gap_pp"])
plt.axhline(0, color="gray", linewidth=1)
plt.title("When Housing Grew Faster than Income (pp difference, 2000+)")
plt.xlabel("Year")
plt.ylabel("Housing % – Income % (percentage points)")
plt.tight_layout()
plt.savefig(PLOT_DIR / "04_growth_gap_recent.png", dpi=300)
plt.close()

df_year = (
    df.groupby("year", as_index=False)[num_cols].mean()
    .sort_values("year")
    .dropna(subset=["median_income_real", "avg_sales_price_real", "afford_ratio_real"])
)
df_recent = df_year[df_year["year"] >= 1990].copy()

base_year = 2000
base = df_recent.loc[df_recent["year"] == base_year]
if base.empty:
    base_year = int(df_recent["year"].iloc[0])
    base = df_recent.iloc[[0]]

base_income = float(base["median_income_real"].iloc[0])
base_price = float(base["avg_sales_price_real"].iloc[0])

income_idx = df_recent["median_income_real"] / base_income * 100.0
price_idx = df_recent["avg_sales_price_real"] / base_price * 100.0

plt.figure(figsize=(8, 4.5))
plt.plot(df_recent["year"], income_idx, label=f"Real income (index, {base_year}=100)")
plt.plot(df_recent["year"], price_idx, label=f"Real avg home price (index, {base_year}=100)")
plt.title("Income vs Home Prices (Both Indexed = 100)")
plt.xlabel("Year")
plt.ylabel("Index")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(PLOT_DIR / "A_indexed_levels.png", dpi=300)
plt.close()

df_recent["afford_ratio_roll5"] = df_recent["afford_ratio_real"].rolling(5, center=True).mean()
plt.figure(figsize=(8, 4.5))
plt.plot(df_recent["year"], df_recent["afford_ratio_real"], alpha=0.25, label="Annual (real)")
plt.plot(df_recent["year"], df_recent["afford_ratio_roll5"], linewidth=2, label="5-yr rolling mean")
plt.title("Affordability: Real Price ÷ Real Income")
plt.xlabel("Year")
plt.ylabel("Ratio (higher = less affordable)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(PLOT_DIR / "B_affordability_smoothed.png", dpi=300)
plt.close()

dec = (
    df_year.assign(decade=(df_year["year"] // 10) * 10)
    .groupby("decade", as_index=False)["afford_ratio_real"]
    .mean()
)
plt.figure(figsize=(8, 4.5))
plt.bar(dec["decade"].astype(str), dec["afford_ratio_real"])
plt.title("Average Affordability Ratio by Decade")
plt.xlabel("Decade")
plt.ylabel("Avg (real price ÷ real income)")
plt.tight_layout()
plt.savefig(PLOT_DIR / "C_affordability_by_decade.png", dpi=300)
plt.close()

df_recent["gap_roll3"] = df_recent["growth_gap_pp"].rolling(3, center=True).mean()
plt.figure(figsize=(8, 4.5))
plt.bar(df_recent["year"], df_recent["growth_gap_pp"], alpha=0.25, label="Annual gap (pp)")
plt.plot(df_recent["year"], df_recent["gap_roll3"], linewidth=2, label="3-yr rolling")
plt.axhline(0, linewidth=1)
plt.title("Housing Growth − Income Growth (percentage points)")
plt.xlabel("Year")
plt.ylabel("pp")
plt.legend()
plt.tight_layout()
plt.savefig(PLOT_DIR / "D_growth_gap_smoothed.png", dpi=300)
plt.close()
