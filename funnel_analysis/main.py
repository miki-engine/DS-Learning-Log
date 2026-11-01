import sqlite3
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = BASE_DIR / "funnel_analysis.db"

CSV_PATHS = {
    "users": DATA_DIR / "users.csv",
    "events": DATA_DIR / "events.csv",
}


def load_csv(csv_path: Path) -> pd.DataFrame:
    """Load a CSV file into a DataFrame.
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


def fetch_overall_funnel(conn: sqlite3.Connection) -> pd.DataFrame:
    """Extract the number of unique users who reached each stage.
    
    Args:
        conn: SQLite database connection.

    Returns:
        DataFrame containing unique user counts for each funnel stage.
    """
    query = """
        SELECT
            e.event_type,
            COUNT(DISTINCT u.user_id) AS funnel_count
        FROM users AS u
        INNER JOIN events AS e
            ON u.user_id = e.user_id
        GROUP BY e.event_type
        ORDER BY
            CASE e.event_type
                WHEN 'view_item' THEN 1
                WHEN 'add_to_cart' THEN 2
                WHEN 'begin_checkout' THEN 3
                WHEN 'purchase' THEN 4
                ELSE 5
            END;
    """

    return pd.read_sql_query(query, conn)


def fetch_segment_funnel(
        conn: sqlite3.Connection,
        segment: str,
) -> pd.DataFrame:
    """Extract the number of unique users who reached each stage
    for each segment.
    """
    pass


def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate overall conversion rate, step-to-step conversion rate,
    and drop-off rate.
    """
    pass


def visualize(df: pd.DataFrame) -> plt.Figure:
    """Create a figure containing funnel charts.
    """
    pass


def save_png(fig: plt.Figure, output_path: Path) -> None:
    """Save the figure as a PNG image.

    Create the destination directory if it does not exist.

    Args:
        fig: Figure containing the funnel charts.
        output_path: Path where the PNG file will be saved.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path)


def print_analysis_report(df: pd.DataFrame) -> None:
    """Print the funnel analysis report.
    """
    pass


def main() -> None:
    """Run funnel analysis workflow."""
    conn = sqlite3.connect(DB_PATH)

    try:
        for table_name, csv_path in CSV_PATHS.items():
            save_to_database(
                load_csv(csv_path),
                table_name,
                conn,
            )

        df = fetch_overall_funnel(conn)

    finally:
        conn.close()

    print(df)


if __name__ == "__main__":
    main()
