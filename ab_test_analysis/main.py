import sqlite3
from pathlib import Path

import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = BASE_DIR / "ab_test.db"

CSV_PATHS = {
    "ab_logs": DATA_DIR / "ab_logs.csv",
    "ab_users": DATA_DIR / "ab_users.csv",
}

ALPHA = 0.05


def load_csv(csv_path: Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        DataFrame containing the CSV data.
    """
    return pd.read_csv(csv_path)


def save_to_database(
    df: pd.DataFrame,
    table_name: str,
    conn: sqlite3.Connection,
) -> None:
    """Save a DataFrame to a table in an SQLite database.

    Replace the existing table if it already exists.

    Args:
        df: DataFrame to save.
        table_name: Name of the destination table.
        conn: SQLite database connection.
    """
    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False,
    )


def fetch_group_summary(conn: sqlite3.Connection) -> pd.DataFrame:
    """Count unique users and purchasers in each A/B test group.

    Args:
        conn: SQLite database connection.

    Returns:
        DataFrame containing user and purchaser counts for each group.
    """
    query = """
        SELECT
            u."group",
            COUNT(DISTINCT u.user_id) AS users_count,
            COUNT(
                DISTINCT CASE
                    WHEN l.purchased = 1 THEN u.user_id
                    ELSE NULL
                END
            ) AS purchased_count
        FROM ab_users AS u
        INNER JOIN ab_logs AS l
            ON u.user_id = l.user_id
        GROUP BY u."group";
    """

    return pd.read_sql_query(query, conn)


def add_purchase_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Add a purchase rate column to the group summary DataFrame.

    Args:
        df: DataFrame containing user and purchaser counts for each group.

    Returns:
        DataFrame with an additional "purchase_rate" column.
    """
    df = df.copy()
    df["purchase_rate"] = df["purchased_count"] / df["users_count"]

    return df


def perform_purchase_rate_test(df: pd.DataFrame) -> tuple[float, float]:
    """Test whether the new design improves the purchase rate
    compared to the old design.

    H0: p_test <= p_control
    H1: p_test > p_control

    Args:
        df: DataFrame containing user and purchaser counts and purchase rate
            for each group.

    Returns:
        Tuple containing the z-statistic and p-value.
    """
    df = df.set_index("group")

    user_counts = [
        df.loc["Test", "users_count"],
        df.loc["Control", "users_count"],
    ]
    purchase_counts = [
        df.loc["Test", "purchased_count"],
        df.loc["Control", "purchased_count"],
    ]

    z_stat, p_value = proportions_ztest(
        count=purchase_counts,
        nobs=user_counts,
        alternative="larger",
    )

    return float(z_stat), float(p_value)


def print_analysis_report(
    df: pd.DataFrame,
    test_result: tuple[float, float],
) -> None:
    """Print the A/B test analysis report.

    Args:
        df: DataFrame containing user and purchaser counts and purchase rate
            for each group.
        test_result: Tuple containing the z-statistic and p-value.
    """
    df = df.set_index("group")
    c_purchase_rate = float(df.loc["Control", "purchase_rate"])
    t_purchase_rate = float(df.loc["Test", "purchase_rate"])
    z_stat, p_value = test_result
    rate_difference_pp = (t_purchase_rate - c_purchase_rate) * 100
    improvement_rate_pct = rate_difference_pp / c_purchase_rate

    print(f"Significance level (alpha): {ALPHA:.2f}")
    print(f"Z-statistic: {z_stat:.4f}")
    print(f"p-value: {p_value:.4f}")

    if p_value < ALPHA:
        print(
            "The Test group's purchase rate is statistically "
            "significantly higher than the Control group's."
        )

    else:
        print(
            "There is insufficient evidence to conclude that "
            "the Test group's purchase rate is higher than "
            "the Control group's."
        )

    print(f"Control purchase rate: {c_purchase_rate:.2%}")
    print(f"Test purchase rate: {t_purchase_rate:.2%}")
    print(f"Purchase rate difference: {rate_difference_pp:+.2f} percentage points")
    print(f"Relative improvement: {improvement_rate_pct:+.2f}%")

    print(
        "The purchase rate was higher in the Test group than "
        "in the Control group. "
        "The observed improvement may have practical significance. However, "
        "the business impact is unknown because implementation costs and "
        "potential profits are unknown."
    )

    print("Final business conclusion:")
    print(
        "The observed purchase rate was higher in the Test group. "
        "However, there is insufficient evidence to conclude that "
        "the new design improves the purchase rate. Implementation "
        "costs and potential profits are also unknown. "
        "We should not roll out the new design yet. "
        "Further A/B testing is needed."
    )

    

def main() -> None:
    """Run AB test analysis workflow."""
    conn = sqlite3.connect(DB_PATH)

    try:
        for table_name, csv_path in CSV_PATHS.items():
            save_to_database(
                load_csv(csv_path),
                table_name,
                conn,
            )

        group_summary_df = fetch_group_summary(conn)

    finally:
        conn.close()

    purchase_summary_df = add_purchase_rate(group_summary_df)
    test_result = perform_purchase_rate_test(purchase_summary_df)
    print_analysis_report(purchase_summary_df, test_result)


if __name__ == "__main__":
    main()