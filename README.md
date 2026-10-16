# Marketing A/B Test Analysis

<img width="1992" height="1152" alt="Marketing A/B test dashboard showing conversion rates and experiment results" src="https://github.com/user-attachments/assets/ace1b860-2819-46c5-816a-f1e394aa3d45" />

[▶ Watch the dashboard demo](https://youtu.be/U3RopPs7UBI)

I built this project to see whether users shown an ad converted more often than a control group shown a public service announcement.

I used Python and SQL for the analysis, a statistical test to compare the conversion rates, and Power BI to build the final dashboard.

## Results

| Metric | Result |
| --- | ---: |
| Ad conversion rate | 2.55% |
| Control conversion rate | 1.79% |
| Absolute lift | +0.77 percentage points |
| Relative lift | +43.09% |
| P-value | < 0.001 |
| 95% confidence interval for the absolute lift | +0.60 to +0.94 percentage points |

The ad group had a 43.09% higher conversion rate than the control group in this dataset. The difference was statistically significant.

## What I did

- Cleaned and checked the raw data with Python
- Stored the cleaned data in SQLite
- Used SQL to compare the two experiment groups
- Tested the difference in conversion rates
- Built the final dashboard in Power BI

The statistical test was a two-sided two-proportion z-test with a 0.05 significance level. The confidence interval estimates the absolute difference between the two conversion rates.

## Dataset

[Marketing A/B Testing - Kaggle](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing)

The dataset contains 588,101 users with experiment group, conversion status, total ads, and the day and hour with the most ads.

The raw CSV is not included in this repository. Download and extract `marketing_AB.csv` from Kaggle and place it in:

```text
data/raw/marketing_AB.csv
```

The notebooks and scripts generate the cleaned CSV, SQLite database, and three dashboard CSVs. These files are kept out of the repository and can be recreated by following the steps below.

## Tools

Python · Pandas · Statsmodels · SQL · SQLite · Jupyter Notebook · Power BI

## Run locally

Tested on Windows with Python 3.14.3. Run the commands from the project folder.

**1. Install the dependencies and start Jupyter.**

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m notebook
```

Use the Python kernel from this environment for both notebooks.

**2. Clean the data.**

Run all cells in `notebooks/01_data_cleaning.ipynb`. This creates `data/cleaned/marketing_ab_cleaned.csv`.

**3. Create the database.**

Open another terminal in the project folder and run:

```powershell
.\.venv\Scripts\python.exe sql/create_database.py
```

This creates `data/marketing_ab_test.db`.

**4. Review the SQL and run the statistical analysis.**

To run the SQL queries, open the database in a SQLite application such as DB Browser for SQLite. In its **Execute SQL** tab, open `sql/analysis.sql` and run the queries.

Then run all cells in `notebooks/02_ab_test_analysis.ipynb`. The notebook reads the database directly, so it does not depend on saving the SQL query results.

**5. Generate the dashboard data.**

```powershell
.\.venv\Scripts\python.exe sql/export_dashboard_data.py
```

This creates these files in `dashboard/`:

- `experiment_dashboard_data.csv`
- `experiment_summary.csv`
- `experiment_metrics.csv`

**6. Open the dashboard.**

Open `dashboard/marketing_ab_test_dashboard.pbix` in Power BI Desktop. It contains imported data, so you can view it straight away.

To refresh it on your computer, go to **Transform data → Data source settings** and change each of the three CSV sources to the files in your local `dashboard/` folder. Apply the changes and refresh.

## Notes

- The ad and control groups are very different in size. I did not independently verify how the original experiment was randomized.
- The dataset does not include campaign cost or revenue, so this project does not measure profitability.
- Dashboard filters affect the charts. The top summary and experiment result describe the full experiment.
- Day and hour refer to when a user saw the most ads, not when they converted. The ad-exposure comparisons do not show that more ads caused conversion.
