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
    """
    """
    pass


def print_basic_statistics(df: pd.DataFrame) -> None:
    """
    """
    pass


def print_group_aggregation(df: pd.DataFrame) -> None:
    """
    """
    pass


def calculate_correlation(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    pass


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
    """Run customer purchase analysis workflow.
    """
    df = load_data(CSV_PATH)
    print_basic_statistics(df)
    print_group_aggregation(df)
    corr_df = calculate_correlation(df)
    fig_heatmap = create_heatmap(corr_df)
    fig_scatterplot = create_scatterplot(df)
    fig_boxplot = create_boxplot(df)
    save_img(fig_heatmap, OUTPUT_PATH_HEATMAP)
    save_img(fig_scatterplot, OUTPUT_PATH_SCATTERPLOT)
    save_img(fig_boxplot, OUTPUT_PATH_BOXPLOT)
    print_insights()


if __name__ == "__main__":
    main()