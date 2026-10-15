"""Export Power BI inputs from the validated SQLite experiment table."""
from pathlib import Path
import sqlite3
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

ROOT = Path(__file__).resolve().parents[1]
database = ROOT / "data" / "marketing_ab_test.db"
if not database.exists():
    raise FileNotFoundError("Run sql/create_database.py before exporting dashboard data.")
with sqlite3.connect(database) as connection:
    data = pd.read_sql_query("SELECT * FROM experiment_data ORDER BY user_id", connection)
if len(data) != 588101 or not data.user_id.is_unique or data.converted.sum() != 14843:
    raise ValueError("Experiment totals do not match the expected dataset.")
summary = data.groupby("test_group").agg(users=("converted", "size"), conversions=("converted", "sum")).reindex(["ad", "psa"])
summary["non_conversions"] = summary.users - summary.conversions
summary["conversion_rate"] = summary.conversions / summary.users
ad, control = summary.conversion_rate
difference = ad - control
_, p_value = proportions_ztest(summary.conversions, summary.users)
standard_error = (ad * (1 - ad) / summary.loc["ad", "users"] + control * (1 - control) / summary.loc["psa", "users"]) ** 0.5
metrics = pd.DataFrame([{
    "ad_conversion_rate": ad,
    "psa_conversion_rate": control,
    "absolute_lift_percentage_points": difference * 100,
    "relative_lift_percent": difference / control * 100,
    "p_value": p_value,
    "ci_lower_percentage_points": (difference - 1.96 * standard_error) * 100,
    "ci_upper_percentage_points": (difference + 1.96 * standard_error) * 100,
}])
output = ROOT / "dashboard"
output.mkdir(exist_ok=True)
data.to_csv(output / "experiment_dashboard_data.csv", index=False)
summary.reset_index().to_csv(output / "experiment_summary.csv", index=False)
metrics.to_csv(output / "experiment_metrics.csv", index=False)
print(f"Exported {len(data):,} users and experiment summaries to dashboard/.")
