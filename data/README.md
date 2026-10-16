# Data

Download and extract `marketing_AB.csv` from [Marketing A/B Testing on Kaggle](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing). Kaggle lists the source dataset as CC0: Public Domain.

Place the file at `data/raw/marketing_AB.csv`. See the main README for the run order.

The cleaning notebook creates `data/cleaned/marketing_ab_cleaned.csv`. The database script creates `data/marketing_ab_test.db`. The export script creates three CSVs in `dashboard/`: `experiment_dashboard_data.csv`, `experiment_summary.csv`, and `experiment_metrics.csv`.

Downloaded and generated data files are ignored by Git. The Power BI file contains imported data.
