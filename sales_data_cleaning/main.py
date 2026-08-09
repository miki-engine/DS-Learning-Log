from pathlib import Path

import pandas as pd


def load_data(csv_path: Path) -> pd.DataFrame:
    """Load dirty user data from a CSV file.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        DataFrame containing dirty user data.
    """
    df = pd.read_csv(csv_path)

    return df


def validate_schema(df: pd.DataFrame) -> None:
    """Validate the schema.

    Args:
        df: DataFrame containing dirty user data.

    Raises:
        ValueError: If one or more required columns are missing.
    """
    expected_columns = {
        "user_id",
        "name",
        "age",
        "signup_date",
        "purchase_amount",
        "status",
    }

    actual_columns = set(df.columns)

    missing = expected_columns - actual_columns
    unexpected = actual_columns - expected_columns

    if missing:
        raise ValueError(f"missing column(s): {sorted(missing)}")

    if unexpected:
        print(f"unexpected column(s): {sorted(unexpected)}")


def clean_name(df: pd.DataFrame) -> pd.DataFrame:
    """Remove leading and trailing whitespace from name values.

    Args:
        df: DataFrame containing dirty user data.

    Returns:
        DataFrame with cleaned name values.
    """
    df_copy = df.copy()
    df_copy["name"] = df_copy["name"].str.strip()

    return df_copy


def clean_age(df: pd.DataFrame) -> pd.DataFrame:
    """Convert age values to a numerical type.

    Args:
        df: DataFrame containing user data.

    Returns:
        DataFrame with age values converted to a numeric type.
    """
    df_copy = df.copy()
    df_copy["age"] = pd.to_numeric(df_copy["age"], errors="coerce")

    return df_copy


def clean_purchase_amount(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    pass


def clean_signup_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    pass


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    pass


def remove_invalid_ages(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    pass


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    pass


def validate_cleaned_data(df: pd.DataFrame) -> None:
    """
    """
    pass


def save_data(df: pd.DataFrame, output_path: Path) -> None:
    """
    """
    pass


def main() -> None:
    """
    """
    pass


if __name__ == "__main__":
    main()