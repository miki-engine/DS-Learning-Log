import sqlite3
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = BASE_DIR / "funnel_analysis.db"

CSV_PATHS = {
    "users": DATA_DIR / "users.csv",
    "events": DATA_DIR / "events.csv",
}

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_PATH_OVERALL = OUTPUT_DIR / "overall_funnel.png"
OUTPUT_PATH_DEVICE = OUTPUT_DIR / "device_funnel.png"
OUTPUT_PATH_TRAFFIC = OUTPUT_DIR / "traffic_source_funnel.png"


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

    Args:
        conn: SQLite database connection.
        segment: Column name used to group users.

    Raises:
        ValueError: If the specified segment is not allowed.

    Returns:
        DataFrame containing unique user counts for each funnel stage,
        grouped by the specified segment.
    """
    allowed_segments = ["device", "traffic_source"]

    if segment not in allowed_segments:
        raise ValueError(f"Invalid segment: {segment}")
    
    query = f"""
        SELECT
            u.{segment},
            e.event_type,
            COUNT(DISTINCT u.user_id) AS funnel_count
        FROM users AS u
        INNER JOIN events AS e
            ON u.user_id = e.user_id
        GROUP BY
            u.{segment},
            e.event_type
        ORDER BY
            u.{segment},
            CASE e.event_type
                WHEN 'view_item' THEN 1
                WHEN 'add_to_cart' THEN 2
                WHEN 'begin_checkout' THEN 3
                WHEN 'purchase' THEN 4
                ELSE 5
            END;
    """

    return pd.read_sql_query(query, conn)


def calculate_indicators(
        df: pd.DataFrame,
        segment: str | None = None,
    ) -> pd.DataFrame:
    """Calculate overall conversion rate, step-to-step conversion rate,
    and drop-off rate.

    Args:
        df: DataFrame containing funnel user counts.
        segment: Column name used for grouping, or None for overall data.

    Returns:
        DataFrame with additional indicator columns.
    """
    df = df.copy()

    if segment is not None:
        initial_count = df.groupby(segment)["funnel_count"].transform("first")
        prev_count = df.groupby(segment)["funnel_count"].shift(1)
    else:
        initial_count = df["funnel_count"].iloc[0]
        prev_count = df["funnel_count"].shift(1)

    df["overall_cvr"] = df["funnel_count"] / initial_count
    df["step_cvr"] = df["funnel_count"] / prev_count
    df["drop_off_rate"] = 1.0 - df["step_cvr"]

    return df


def add_transition_column(
    df: pd.DataFrame,
    segment: str | None = None,
) -> pd.DataFrame:
    """Add transition column to DataFrame.

    Args:
        df: DataFrame containing funnel user counts and indicator columns.
        segment: Column name used for grouping, or None for overall data.

    Returns:
        DataFrame with an additional transition column.
    """
    df = df.copy()

    if segment is not None:
        previous_event = df.groupby(segment)["event_type"].shift(1)
    else:
        previous_event = df["event_type"].shift(1)

    df["transition"] = (
        previous_event
        + " → "
        + df["event_type"]
    )

    return df


def add_drop_off_number_column(
    df: pd.DataFrame,
    segment: str | None = None,
) -> pd.DataFrame:
    """Add drop-off column to DataFrame.

    Args:
        df: DataFrame containing funnel user counts, indicator columns,
        and transition column.
        segment: Column name used for grouping, or None for overall data.

    Returns:
        DataFrame with an additional drop-off column.
    """
    df = df.copy()

    if segment is not None:
        prev_count = df.groupby(segment)["funnel_count"].shift(1)
    else:
        prev_count = df["funnel_count"].shift(1)

    df["drop_off_number"] = prev_count - df["funnel_count"]

    return df


def visualize_overall(df: pd.DataFrame) -> plt.Figure:
    """Create a figure containing funnel charts.

    Args:
        df: DataFrame containing funnel user counts and indicator columns.

    Returns:
        Figure showing funnel user counts and step-to-step drop-off rates.
    """
    fig, axes = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(12, 8),
    )

    sns.barplot(
        data=df,
        x="funnel_count",
        y="event_type",
        errorbar=None,
        ax=axes[0],
    )
    axes[0].bar_label(
        axes[0].containers[0],
        fmt="{:,.0f}",
        padding=3,
        fontsize=10,
    )
    axes[0].margins(x=0.15)
    axes[0].set_title("Funnel Chart")
    axes[0].set_xlabel("Funnel Count")
    axes[0].set_ylabel("Event Type")

    dropoff_df = df.dropna(subset=["drop_off_rate"])

    sns.barplot(
        data=dropoff_df,
        x="transition",
        y="drop_off_rate",
        errorbar=None,
        ax=axes[1],
    )
    axes[1].bar_label(
        axes[1].containers[0],
        fmt=lambda x: f"{x*100:.2f}%",
        padding=3,
        fontsize=10,
    )
    axes[1].set_ylim(0, 1.0)
    axes[1].yaxis.set_major_formatter(PercentFormatter(xmax=1.0))
    axes[1].set_title("Drop-off Rate between Funnel Steps")
    axes[1].set_xlabel("Transition")
    axes[1].set_ylabel("Drop-off Rate (%)")

    fig.tight_layout()

    return fig


def visualize_segment(
        df: pd.DataFrame,
        segment: str,
) -> plt.Figure:
    """Create a figure showing funnel drop-off rates by segment.

    Args:
        df: DataFrame containing funnel user counts and indicator columns by segments.
        segment: Column name used for grouping.

    Returns:
        Figure showing step-to-step drop-off rates by segments.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    dropoff_df = df.dropna(subset=["drop_off_rate"])

    sns.barplot(
        data=dropoff_df,
        x="transition",
        y="drop_off_rate",
        hue=segment,
        errorbar=None,
        ax=ax,
    )
    for container in ax.containers:
        ax.bar_label(
            container,
            fmt=lambda x: f"{x*100:.2f}%",
            padding=3,
            fontsize=10,
        )

    segment_label = segment.replace("_", " ").title()

    ax.set_title(f"Drop-off Rate between Funnel Steps by {segment_label}")
    ax.legend(title=segment_label)

    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0))
    ax.set_xlabel("Transition")
    ax.set_ylabel("Drop-off Rate (%)")

    fig.tight_layout()

    return fig


def save_png(fig: plt.Figure, output_path: Path) -> None:
    """Save the figure as a PNG image.

    Create the destination directory if it does not exist.

    Args:
        fig: Figure containing the funnel charts.
        output_path: Path where the PNG file will be saved.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path)


def print_overall_report(df: pd.DataFrame) -> None:
    """Print the overall funnel analysis report.

    Args:
        df: DataFrame containing funnel user counts and indicator columns.
    """
    final_cvr = df.loc[
        df["event_type"] == "purchase",
        "overall_cvr"
    ].iloc[0]

    max_drop_point = df["drop_off_rate"].idxmax()
    max_drop_rate = df.loc[max_drop_point, "drop_off_rate"]
    max_rate_transition = df.loc[max_drop_point, "transition"]

    max_drop_number_point = df["drop_off_number"].idxmax()
    max_drop_number = df.loc[max_drop_number_point, "drop_off_number"]
    max_transition = df.loc[max_drop_number_point, "transition"]

    print(f"Final Purchase Conversion Rate: {final_cvr:.2%}")
    print(f"Maximum Drop-off: {max_transition} ({max_drop_number:.0f} users)")
    print(f"Maximum Drop-off Rate: {max_rate_transition} {max_drop_rate:.2%}")


def print_segment_report(
        df: pd.DataFrame,
        segment: str,
) -> None:
    """Print the funnel analysis report by segments.

    Args:
        df: DataFrame containing funnel user counts and indicator columns by segments.
        segment: Column name used for grouping.
    """
    for segment_value, segment_df in df.groupby(segment):
        final_cvr = segment_df.loc[
            segment_df["event_type"] == "purchase",
            "overall_cvr"
        ].iloc[0]

        max_drop_point = segment_df["drop_off_rate"].idxmax()
        max_drop_rate = segment_df.loc[max_drop_point, "drop_off_rate"]
        max_rate_transition = segment_df.loc[max_drop_point, "transition"]

        max_drop_number_point = segment_df["drop_off_number"].idxmax()
        max_drop_number = segment_df.loc[max_drop_number_point, "drop_off_number"]
        max_transition = segment_df.loc[max_drop_number_point, "transition"]

        print(f"=== {segment_value} ===")

        print(f"Final Purchase Conversion Rate: {final_cvr:.2%}")
        print(f"Maximum Drop-off: {max_transition} ({max_drop_number:.0f} users)")
        print(f"Maximum Drop-off Rate: {max_rate_transition} {max_drop_rate:.2%}")


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
        device_df = fetch_segment_funnel(conn, "device")
        traffic_df = fetch_segment_funnel(conn, "traffic_source")
    finally:
        conn.close()

    df = calculate_indicators(df)
    device_df = calculate_indicators(device_df, segment="device")
    traffic_df = calculate_indicators(traffic_df, segment="traffic_source")

    df = add_transition_column(df)
    device_df = add_transition_column(device_df, segment="device")
    traffic_df = add_transition_column(traffic_df, segment="traffic_source")

    df = add_drop_off_number_column(df)
    device_df = add_drop_off_number_column(device_df, segment="device")
    traffic_df = add_drop_off_number_column(traffic_df, segment="traffic_source")

    print_overall_report(df)
    print_segment_report(device_df, segment="device")
    print_segment_report(traffic_df, segment="traffic_source")

    fig_overall = visualize_overall(df)
    save_png(fig_overall, OUTPUT_PATH_OVERALL)

    fig_device = visualize_segment(device_df, "device")
    fig_traffic = visualize_segment(traffic_df, "traffic_source")
    save_png(fig_device, OUTPUT_PATH_DEVICE)
    save_png(fig_traffic, OUTPUT_PATH_TRAFFIC)

    plt.show()
    plt.close(fig_overall)
    plt.close(fig_device)
    plt.close(fig_traffic)


if __name__ == "__main__":
    main()
