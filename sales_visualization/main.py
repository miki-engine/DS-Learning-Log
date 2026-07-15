from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(csv_path: Path) -> pd.DataFrame:
    """
    """
    pass

def aggregate_sales(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """
    """
    pass


def visualize(daily_sales: pd.Series, category_sales: pd.Series) -> plt.Figure:
    """
    """
    pass


def save_png(fig: plt.Figure, output_path: Path) -> None:
    """
    """
    pass