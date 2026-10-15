# Marketing A/B Test Analysis

<img width="1992" height="1152" alt="Marketing A/B Test Dashboard" src="https://github.com/user-attachments/assets/a85670b6-2bb7-405d-8ffd-4d43b3d4aae9" />

I built this project to see whether showing an ad improved conversion compared with a control group that was shown a Public Service Announcement.

I used Python and SQL for the analysis, statistical testing to validate the result, and Power BI to build the final dashboard.

## Results

| Metric | Result |
| --- | ---: |
| Ad conversion rate | 2.55% |
| Control conversion rate | 1.79% |
| Absolute lift | +0.77 percentage points |
| Relative lift | +43.09% |
| P-value | < 0.001 |
| 95% confidence interval | +0.60 to +0.94 percentage points |

The ad group performed better than the control group in this dataset.

## What I did

- Cleaned and checked the raw data with Python
- Stored the cleaned data in SQLite
- Used SQL to compare the two experiment groups
- Tested the difference in conversion rates
- Built the final dashboard in Power BI

## Dataset

[Marketing A/B Testing - Kaggle](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing)

The dataset contains 588,101 users with experiment group, conversion status, total ads, and the day and hour with the most ads.

The raw CSV is not included in this repository. Download `marketing_AB.csv` from Kaggle and place it in:

```text
data/raw/marketing_AB.csv
```

## Tools

Python · Pandas · Statsmodels · SQL · SQLite · Jupyter Notebook · Power BI

## Run locally

```bash
pip install -r requirements.txt
```

Run `notebooks/01_data_cleaning.ipynb`, then:

```bash
python sql/create_database.py
```

Run `sql/analysis.sql`, then open `notebooks/02_ab_test_analysis.ipynb`.

## Notes

- The Ad and Control groups are very different in size.
- I did not independently verify how the original experiment was randomized.
- The dataset does not include campaign cost or revenue, so this project does not measure profitability.
