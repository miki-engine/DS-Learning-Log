from pathlib import Path

import pandas as pd


def analyze_sales_cross_tab(logs):
    """
    Create a cross-tab pivot table summarizing sales amount by rank and category.

    Args:
        logs: A list of dictionaries or DataFrame containing sales log data
        (customer_id, rank, category, amount).

    Returns:
        pandas.DataFrame: A pivot table with rank as index, category as columns,
        and total amount as values.
    """
    sales_logs = pd.DataFrame(logs)

    result = pd.pivot_table(
        sales_logs,
        index="rank",
        columns="category",
        values="amount",
        aggfunc="sum",
        fill_value=0
    )

    return result


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data" / "sales_logs.csv"

    sales_logs = pd.read_csv(csv_path)

    result = analyze_sales_cross_tab(sales_logs)
    print(result)