from pathlib import Path
import pandas as pd


def load_data(data_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load users and purchases CSV files into DataFrames.
    
    Args:
        data_dir: Path to the directory containing the CSV files.
        
    Returns:
        A tuple of (users_df, purchases_df)
    """
    pass


def merge_data(users_df: pd.DataFrame, purchases_df: pd.DataFrame) -> pd.DataFrame:
    """Merge user master data with purchase logs on user_id
    
    Args:
        users_df: User master data (user_id, name, membership).
        purchases_df: Purchase log data (purchase_id, user_id, amount, category).
        
    Returns:
        Merged DataFrame containing purchase recourds with membership info.
    """pass


def analyze_sales_by_membership(merged_df: pd.DataFrame) -> pd.Series:
    """Aggregate total purchase amount by membership rank.

    Args:
        merged_df Merged DataFrame containing "membership" and "amount" columns.

    Returns:
        Series indexed by membership rank with summed amounts.
    """
    pass


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data"

    users_df, purchase_df = load_data(data_dir)
    merged_df = merge_data(users_df, purchase_df)
    result = analyze_sales_by_membership(merged_df)

    print(result)