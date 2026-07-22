from pathlib import Path

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(data_dir: Path) -> pd.DataFrame:
    """Load sales logs CSV file into DataFrame.

    Args:
        data_dir: Path to the directory containing the CSV file.

    Returns:
        DataFrame containing sales log data.
    """
    pass


def filter_by_category(
        df: pd.DataFrame,
        categories: list[str],
) -> pd.DataFrame:
    """Filter a DataFrame by category.

    Args:
        df: DataFrame containing sales log data.
        category: Category to use for filtering.

    Returns:
        DataFrame containing rows that match the selected category.
    """
    pass


def create_category_sales_chart(category_df: pd.DataFrame) -> plt.Figure:
    """Create a figure from data filtered by category.

    Args:
        category_df: DataFrame filtered by the selected category.

    Returns:
        Figure showing sales data for the selected category.
    """
    pass