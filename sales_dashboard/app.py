from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


@st.cache_data
def load_data(data_dir: Path) -> pd.DataFrame:
    """Load sales logs CSV file into DataFrame.

    Args:
        data_dir: Path to the directory containing the CSV file.

    Returns:
        DataFrame containing sales log data.
    """
    csv_path = data_dir / "sales_logs.csv"
    df = pd.read_csv(csv_path, parse_dates=["date"])

    return df


def filter_by_category(
    df: pd.DataFrame,
    categories: list[str],
) -> pd.DataFrame:
    """Filter a DataFrame by category.

    Args:
        df: DataFrame containing sales log data.
        categories: Categories to use for filtering.

    Returns:
        DataFrame containing rows that match the selected categories.
    """
    category_df = df[df["category"].isin(categories)]

    return category_df


def create_category_sales_chart(category_df: pd.DataFrame) -> plt.Figure:
    """Create a figure from data filtered by category.

    Args:
        category_df: DataFrame filtered by the selected categories.

    Returns:
        Figure showing sales data for the selected categories.
    """
    daily_category_sales = (
        category_df.groupby(["date", "category"], as_index=False)["amount"]
        .sum()
        .sort_values(["date", "category"])
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.lineplot(
        data=daily_category_sales,
        x="date",
        y="amount",
        hue="category",
        marker="o",
        ax=ax,
    )
    ax.set_title("Daily Sales by Category")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales Amount")

    fig.tight_layout()

    return fig


st.title("Sales Analysis Dashboard")
st.write("Selecting categories will allow you to see the daily sales trends.")

base_dir = Path(__file__).resolve().parent
data_dir = base_dir / "data"
df = load_data(data_dir)

categories = sorted(
    df["category"].dropna().unique().tolist()
)

selected_categories = st.sidebar.multiselect(
    label="Select categories",
    options=categories,
    default=categories,
)

if not selected_categories:
    st.info("Please select at least one category.")
    st.stop()

category_df = filter_by_category(
    df,
    selected_categories,
)

st.dataframe(category_df)

fig = create_category_sales_chart(category_df)
st.pyplot(fig)
plt.close(fig)