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

    Raises:
        ValueError: If all users have the same purchase outcome.

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

    total_purchases = sum(purchase_counts)
    total_users = sum(user_counts)

    if total_purchases == 0:
        raise ValueError(
            "Cannot perform the z-test: no purchases were observed."
        )

    if total_purchases == total_users:
        raise ValueError(
            "Cannot perform the z-test: no non-purchasers were observed."
        )

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

    rate_difference = t_purchase_rate - c_purchase_rate
    rate_difference_pp = rate_difference * 100

    if c_purchase_rate == 0:
        relative_change_pct = None
    else:
        relative_change_pct = (rate_difference / c_purchase_rate) * 100

    print("A/B Test Analysis Report")
    print("-" * 40)

    print("1. Purchase Rate Summary")
    print(f"Control purchase rate: {c_purchase_rate:.2%}")
    print(f"Test purchase rate: {t_purchase_rate:.2%}")
    print(
        "Purchase rate difference: "
        f"{rate_difference_pp:+.2f} percentage points"
    )

    if relative_change_pct is None:
        print("Relative change: N/A (Control purchase rate is 0%)")
    else:
        print(f"Relative change: {relative_change_pct:+.2f}%")

    print("-" * 40)

    print("2. Statistical Test")

    print(f"Significance level (alpha): {ALPHA:.2f}")
    print(f"Z-statistic: {z_stat:.4f}")
    print(f"p-value: {p_value:.4f}")

    print("-" * 40)

    print("3. Statistical Interpretation")

    if p_value <= ALPHA:
        print(
            "The Test group's purchase rate is statistically "
            "significantly higher than the Control group's."
        )

    elif t_purchase_rate > c_purchase_rate:
        print(
            "The purchase rate was higher in the Test group than "
            "in the Control group. However, there is insufficient "
            "evidence to conclude that the new design improves the "
            "purchase rate."
        )

    else:
        print(
            "The Test group's observed purchase rate was not "
            "higher than the Control group's."
        )

    print("-" * 40)

    print("4. Practical Significance")

    if rate_difference_pp > 0:
        print("The observed increase may have business value.")

    elif rate_difference_pp < 0:
        print("The observed decrease may have a negative business impact.")

    else:
        print("No difference in purchase rates was observed.")

    print(
        "The practical significance cannot be determined "
        "because implementation costs and expected profits are unknown, "
        "and the true effect of the new design remains uncertain."
    )

    print("-" * 40)

    print("5. Business Recommendation")

    if p_value <= ALPHA:
        print(
            "There is statistically significant evidence that "
            "the new design improves the purchase rate. "
            "If the expected benefits outweigh the implementation "
            "costs, we should consider rolling out the new design."
        )

    elif rate_difference_pp > 0:
        print(
            "The observed purchase rate was higher in the Test group. "
            "However, there is insufficient evidence to conclude that "
            "the new design improves the purchase rate. Implementation "
            "costs and potential profits are also unknown. "
            "We should not roll out the new design yet. "
            "Before conducting another A/B test, we should determine the "
            "minimum detectable effect and calculate the required sample "
            "size through a power analysis. We should also evaluate "
            "potential revenue gains and implementation costs."
        )

    else:
        print(
            "No improvement in the purchase rate was observed, "
            "and there is no statistically significant evidence "
            "that the new design improves the purchase rate. "
            "We should not roll out the new design based on "
            "the current results. The design should be reviewed "
            "before further testing."
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