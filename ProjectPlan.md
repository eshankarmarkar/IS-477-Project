 Overview
•	Our project will look at how unaffordable the housing market has become over the past couple of years (5-10 years).
•	We will compare income levels and house prices to see how much faster prices are rising than incomes.
•	The goal is to show where and how housing has become harder to afford.
•	This is valuable because it helps explain the growing cost of living problem and housing inequality in the U.S.
•	We will follow a clear data lifecycle from collection → cleaning → integration → analysis → visualization → reporting, ensuring a structured and reproducible workflow.
•	Our data will be mainly from government sources such as FRED and the U.S. census bureau 
Research Questions
•	How has housing affordability changed over the past year?
•	How do changes in income compare to changes in home prices?
•	Which states or cities have become the least affordable?
•	These questions will be answered through data integration and analysis using Python (Pandas) to combine and visualize patterns between income and housing prices.
Members: Eshan Karmarkar and Victor Samuel
•	Work Split: We will split all work evenly and both contribute to coding, analysis, and writing.
•	Eshan’s main tasks:
o	Find and clean income data 
o	Find and clean housing data 
o	Help write the report and handle GitHub setup
•	Victor’s main tasks:
o	Analyze and visualize data (graphs, charts, trends)
o	Help with calculations and writing the final report
o	Set up workflow automation and organization
•	 We will use Git and GitHub for version control to track contributions and ensure reproducibility 
•	All files and notebooks will be organized under clear folders (data/raw, data/clean, scripts, output) following best practices from the data lifecycle and provenance modules.
Datasets
•	Dataset 1: Census Income Tables (U.S. Census Bureau — “Income in the United States: 2024”) Census.gov
o	Table A-1: Income Summary Measures by Selected Characteristics (2023 & 2024)
o	Table A-2: Households by Total Money Income by race/Hispanic origin (1967–2024)
o	Median Household Income & Median Earnings by Educational Attainment (2004–2024)
o	Format: downloadable spreadsheets (XLS) < ~1.0 MB each Census.gov
o	Key variables: median household income, distribution by income brackets, earnings by education, possibly demographic breakdowns
•	Dataset 2: Housing Price Data (FRED / St. Louis Fed) — ASPUS / MSPUS series FRED
o	“Average Sales Price of Houses Sold for the U.S.” (ASPUS) — quarterly data, dollars, not seasonally adjusted FRED
o	Also possibly “Median Sales Price of Houses Sold for the U.S.” (MSPUS) — if available from FRED
o	Format: timeseries data retrievable via FRED API or CSV download
•	Integration and Cleaning Plan:
o	We will merge the datasets by year using Python (Pandas).
o	Missing values will be handled through imputation or removal, and data will be standardized (e.g., converting to 2024 dollars if needed).
o	Data quality will be checked for missing values, outliers, and year alignment to ensure accuracy.
o	All cleaning and integration steps will be documented to maintain workflow provenance.
Timeline:

During Week 1 (October 5 – October 11); Eshan and Victor after we have selected our potential datasets, we will be using will finalize the datasets that we will actually select. The dataset will be selected from the U.S. Census Bureau and how we’d find housing prices is through FRED. Both members will inspect data formats and record detailed metadata, ensuring all files are properly organized under.
In Week 2 (October 12-18) Eshan will take charge of data cleaning with things such as renaming columns, changing data formats, and analyzing missing/incomplete values. Ensuring values are adjusted for inflations and cleaned datasets will be stored in a new file.
By Week 3 (October 19- 25) Both Members will look towards merging income and datasets by years (from the last 5-10) making sure their consistent units. 
During Week 4 (October 26 -November 1) Victor will conduct analysis to compute ratios on affordability, percent changes with housing and income, and initial correlations between income growth and housing price growth. Visualizations can start to be developed in this stage.
In Week 5 (November 2- November 8) Conduct deeper analysis to identify which states and regions have experienced the largest declines in affordability. This stage will also include drafting sections of the written report and refining the statistical measures used in the analysis.
During Week 6 (November 9- November 15) Victor refines components of the dataset and makes sure we ensure all visualizations are properly labeled, clear legend key, and proper formatting.
In Week 7(November 16-22) We will compile the final markdown report, incorporate feedback, and prepare the GitHub release. The completed project containing all notebooks, cleaned datasets, and visual outputs
Constraints:
-	Census data is annual while FRED housing data is quarterly alignment will require aggregation.
-	Historical Census tables may change variable names or structures over time.
-	Potential inconsistencies in units (nominal vs real dollars).
-	Two-person team with limited time for deep econometric modeling; focus will remain on descriptive and comparative analysis.
Gaps 
Week 2 – Data Ethics, Laws, and Governance
-	We need to confirm compliance with FRED and Census data-use policies and clarify citation requirements as we learn more about ethical data governance.
-	Additional input may be needed on how to identify and communicate potential demographic or geographic biases that could influence affordability trends.
Weeks 3–5 Data Collection, Storage, and Relational Model
-	Could reconstruct projects' data into regional databases for income and housing prices once we learn best practice for schema design 
Weeks 6–8 Extraction, Enrichment, and Integration
-	We plan to expand beyond simple year-based mergers after learning more advanced schema and record level integration methods later in the course.
-	We anticipate incorporating enrichment steps such as inflation adjustments or regional mapping once we understand how to apply them systematically.
Weeks 11–12   Workflow Automation, Data Lineage, and Provenance
-	As we learn about workflow automation, we aim to create reproducible scripts or pipelines to automate cleaning and integration tasks.
-	We will need to document all data transformations more rigorously to maintain full provenance and transparency.
