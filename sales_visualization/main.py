from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(data_dir: Path) -> pd.DataFrame:
    """Load sales logs CSV file into DataFrame.

    Args:
        data_dir: Path to the directory containing the CSV file.

    Returns:
        DataFrame containing sales logs data (date, category, amount).
    """
    csv_path = data_dir / "sales_logs.csv"
    df = pd.read_csv(csv_path, parse_dates=["date"])

    return df


def aggregate_sales(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Aggregate daily sales and total sales by category.

    Args:
        df: DataFrame containing sales log data
            (date, category, amount).

    Returns:
        Tuple containing daily sales and sales by category.
    """
    daily_sales = (
        df.groupby("date", as_index=False)["amount"]
        .sum()
        .sort_values("date")
    )

    category_sales = (
        df.groupby("category", as_index=False)["amount"]
        .sum()
    )

    return daily_sales, category_sales


def visualize(
    daily_sales: pd.DataFrame,
    category_sales: pd.DataFrame,
) -> plt.Figure:
    """Create a figure containing two sales charts.

    The top chart shows the daily sales trend, and the bottom chart
    shows total sales by category.

    Args:
        daily_sales: DataFrame containing daily sales
            (date, amount).
        category_sales: DataFrame containing sales by category
            (category, amount).

    Returns:
        Figure containing a line chart and a bar chart.
    """
    fig, axes = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(12, 8),
    )

    sns.lineplot(
        data=daily_sales,
        x="date",
        y="amount",
        marker="o",
        ax=axes[0],
    )
    axes[0].set_title("Total Daily Sales")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Sales Amount")

    sns.barplot(
        data=category_sales,
        x="category",
        y="amount",
        errorbar=None,
        ax=axes[1],
    )
    axes[1].set_title("Total Sales by Category")
    axes[1].set_xlabel("Category")
    axes[1].set_ylabel("Sales Amount")

    fig.tight_layout()

    return fig


def save_png(fig: plt.Figure, output_path: Path) -> None:
    """Save the figure as a PNG image.

    Create the destination directory if it does not exist.

    Args:
        fig: Figure containing the sales charts.
        output_path: Path where the PNG file will be saved.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path)


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"
    output_path = base_dir / "output" / "sales_report.png"

    df = load_data(data_dir)
    daily_sales, category_sales = aggregate_sales(df)
    fig = visualize(daily_sales, category_sales)
    save_png(fig, output_path)
    plt.show()