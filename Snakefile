rule run_all:
    input:
        "output/plots/01_income_vs_price_real.png",
        "output/plots/02_affordability_ratio.png",
        "output/plots/03_yoy_growth_recent.png",
        "output/plots/04_growth_gap_recent.png",
        "output/plots/A_indexed_levels.png",
        "output/plots/B_affordability_smoothed.png",
        "output/plots/C_affordability_by_decade.png",
        "output/plots/D_growth_gap_smoothed.png"

rule acquire_fred:
    output:
        "data/raw/housing_fred.json",
        "data/raw/cpi_fred.json"
    shell:
        "python src/acquire_fred.py"

rule clean_income:
    input:
        "data/raw/incomedata.csv"
    output:
        "data/clean/income_clean.csv"
    shell:
        "python src/clean_income.py"

rule clean_fred:
    input:
        "data/raw/housing_fred.json",
        "data/raw/cpi_fred.json"
    output:
        "data/clean/housing_clean.csv",
        "data/clean/cpi_clean.csv"
    shell:
        "python src/clean_housing_cpi.py"

rule merge_affordability:
    input:
        "data/clean/housing_clean.csv",
        "data/clean/income_clean.csv",
        "data/clean/cpi_clean.csv"
    output:
        "data/clean/merged_affordability.csv"
    shell:
        "python src/merge_affordability.py"

rule make_plots:
    input:
        "data/clean/merged_affordability.csv"
    output:
        "output/plots/01_income_vs_price_real.png",
        "output/plots/02_affordability_ratio.png",
        "output/plots/03_yoy_growth_recent.png",
        "output/plots/04_growth_gap_recent.png",
        "output/plots/A_indexed_levels.png",
        "output/plots/B_affordability_smoothed.png",
        "output/plots/C_affordability_by_decade.png",
        "output/plots/D_growth_gap_smoothed.png"
    shell:
        "python src/make_plots.py"
