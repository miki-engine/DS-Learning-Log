from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(data_dir: Path) -> pd.DataFrame:
    """Load sales logs CSV file into DataFrame.

    Args:
        data_dir: Path to the directory containing the CSV file.

    Returns:
        DataFrame containing sales logs data (date, category, amount)
    """
    csv_path = data_dir / "sales_logs.csv"
    df = pd.read_csv(csv_path, parse_dates=["date"])

    return df


def aggregate_sales(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Aggregate daily total sales and total sales by category.

    Args:
        df: DataFrame containing sales logs data (date, category, amount)

    Returns:
        Tuple of total daily sales and total sales by category.
    """
    daily_sales = df.groupby("date")["amount"].sum()
    category_sales = df.groupby("category")["amount"].sum()

    return daily_sales, category_sales


def visualize(daily_sales: pd.Series, category_sales: pd.Series) -> plt.Figure:
    """
    """
    pass


def save_png(fig: plt.Figure, output_path: Path) -> None:
    """
    """
    pass


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"

    output_path = base_dir / "output" / "sales_visualization.png"