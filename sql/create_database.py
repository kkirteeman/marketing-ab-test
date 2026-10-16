import csv
import sqlite3
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "cleaned" / "marketing_ab_cleaned.csv"
DATABASE_PATH = PROJECT_ROOT / "data" / "marketing_ab_test.db"


def converted_to_integer(value):
    if value == "True":
        return 1
    if value == "False":
        return 0
    raise ValueError(f"Unexpected converted value: {value}")


if not CSV_PATH.is_file():
    raise FileNotFoundError("Run notebooks/01_data_cleaning.ipynb before creating the database.")

with CSV_PATH.open(newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    rows = [
        (
            int(row["user_id"]),
            row["test_group"],
            converted_to_integer(row["converted"]),
            int(row["total_ads"]),
            row["most_ads_day"],
            int(row["most_ads_hour"]),
        )
        for row in reader
    ]

with sqlite3.connect(DATABASE_PATH) as connection:
    connection.execute("BEGIN")
    connection.execute("DROP TABLE IF EXISTS experiment_data")
    connection.execute(
        """
        CREATE TABLE experiment_data (
            user_id INTEGER PRIMARY KEY,
            test_group TEXT NOT NULL,
            converted INTEGER NOT NULL CHECK (converted IN (0, 1)),
            total_ads INTEGER NOT NULL,
            most_ads_day TEXT NOT NULL,
            most_ads_hour INTEGER NOT NULL
        )
        """
    )
    connection.executemany(
        """
        INSERT INTO experiment_data
        (user_id, test_group, converted, total_ads, most_ads_day, most_ads_hour)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        rows,
    )

    final_row_count = connection.execute(
        "SELECT COUNT(*) FROM experiment_data"
    ).fetchone()[0]
    unique_user_count = connection.execute(
        "SELECT COUNT(DISTINCT user_id) FROM experiment_data"
    ).fetchone()[0]
    group_values = {
        row[0]
        for row in connection.execute(
            "SELECT DISTINCT test_group FROM experiment_data"
        )
    }
    conversion_total = connection.execute(
        "SELECT SUM(converted) FROM experiment_data"
    ).fetchone()[0]

    if final_row_count != 588101:
        raise ValueError(f"Expected 588101 rows, found {final_row_count}")
    if unique_user_count != final_row_count:
        raise ValueError("User IDs are not unique")
    if group_values != {"ad", "psa"}:
        raise ValueError(f"Unexpected experiment groups: {group_values}")
    if conversion_total != 14843:
        raise ValueError(f"Expected 14843 conversions, found {conversion_total}")

print(f"Database created: {DATABASE_PATH}")
print("Table created: experiment_data")
print(f"Rows: {final_row_count}")
print(f"Unique user IDs: {unique_user_count}")
print(f"Experiment groups: {sorted(group_values)}")
print(f"Conversions: {conversion_total}")
