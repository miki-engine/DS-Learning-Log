from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "web_behavior_data.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_PATH_HEATMAP = OUTPUT_DIR / "heatmap.png"
OUTPUT_PATH_SCATTERPLOT = OUTPUT_DIR / "scatterplot.png"
OUTPUT_PATH_BOXPLOT = OUTPUT_DIR / "boxplot.png"


def load_data(csv_path: Path) -> pd.DataFrame:
    """Load customer web behavior data CSV file into DataFrame.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        DataFrame containing customer web behavior data.
    """
    return pd.read_csv(csv_path)


def print_basic_statistics(df: pd.DataFrame) -> None:
    """Print basic statistics of the data.

    Args:
        df: DataFrame containing customer web behavior data.
    """
    print(df.describe())


def print_group_aggregation(df: pd.DataFrame) -> None:
    """Compare mean numerical values between buyers and non-buyers.

    Args:
        df: DataFrame containing customer web behavior data.
    """
    columns = [
        "age",
        "site_visits",
        "time_on_site_min",
        "pages_viewed",
    ]

    purchase_group_means = df.groupby("purchased")[columns].mean()

    print(purchase_group_means)


def calculate_correlation(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate the correlation coefficient between each variable.

    Args:
        df: DataFrame containing customer web behavior data.

    Returns:
        corr_df: DataFrame including correlation coefficients between all variables.
    """
    corr_df = df.select_dtypes(include="number").corr()

    return corr_df


def print_correlation_matrix(corr_df: pd.DataFrame) -> None:
    """Print the correlation matrix.

    Args:
        corr_df: DataFrame including correlation coefficients between all variables.
    """
    print(corr_df)


def print_purchase_correlation(corr_df: pd.DataFrame) -> None:
    """Print the correlations with the purchased variable.

    Args:
        corr_df: DataFrame including correlation coefficients between all variables.
    """
    purchased_corr = corr_df["purchased"]
    purchased_corr_dropped = purchased_corr.drop("purchased")
    sorted_corr = purchased_corr_dropped.sort_values(
        key=abs,
        ascending=False,
    )

    print(sorted_corr)


def create_heatmap(corr_df: pd.DataFrame) -> plt.Figure:
    """
    """
    pass


def create_scatterplot(df: pd.DataFrame) -> plt.Figure:
    """
    """
    pass


def create_boxplot(df: pd.DataFrame) -> plt.Figure:
    """
    """
    pass


def save_img(fig: plt.Figure, output_path: Path) -> None:
    """
    """
    pass


def print_insights() -> None:
    """
    """
    pass


def main() -> None:
    """Run customer purchase analysis workflow."""
    df = load_data(CSV_PATH)
    print_basic_statistics(df)
    print_group_aggregation(df)
    corr_df = calculate_correlation(df)
    print_correlation_matrix(corr_df)
    print_purchase_correlation(corr_df)
    fig_heatmap = create_heatmap(corr_df)
    fig_scatterplot = create_scatterplot(df)
    fig_boxplot = create_boxplot(df)
    save_img(fig_heatmap, OUTPUT_PATH_HEATMAP)
    save_img(fig_scatterplot, OUTPUT_PATH_SCATTERPLOT)
    save_img(fig_boxplot, OUTPUT_PATH_BOXPLOT)
    print_insights()


if __name__ == "__main__":
    main()