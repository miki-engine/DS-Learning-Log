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
    """Convert age values to a numeric type.

    Args:
        df: DataFrame containing user data.

    Returns:
        DataFrame with age values converted to a numeric type.
    """
    df_copy = df.copy()
    df_copy["age"] = pd.to_numeric(df_copy["age"], errors="coerce")

    return df_copy


def clean_purchase_amount(df: pd.DataFrame) -> pd.DataFrame:
    """Remove unnecessary characters from purchase amount values and 
    convert them to a numeric type.

    Args:
        df: DataFrame containing user data.

    Returns:
        DataFrame with purchase amount values converted to a numeric type.
    """
    df_copy = df.copy()

    df_copy["purchase_amount"] = (
        df_copy["purchase_amount"]
        .astype("string")
        .str.replace("[¥,]", "", regex=True)
    )

    df_copy["purchase_amount"] = pd.to_numeric(
        df_copy["purchase_amount"],
        errors="coerce",
    )

    return df_copy


def clean_signup_date(df: pd.DataFrame) -> pd.DataFrame:
    """Convert signup date values to a datetime type.

    Args:
        df: DataFrame containing user data.

    Returns:
        DataFrame with signup date values converted to a datetime type.
    """
    df_copy = df.copy()

    df_copy["signup_date"] = (
        df_copy["signup_date"]
        .astype("string")
        .str.replace("/", "-", regex=False)
    )

    parsed_full_year = pd.to_datetime(
        df_copy["signup_date"],
        format="%Y-%m-%d",
        errors="coerce",
    )

    parsed_short_year = pd.to_datetime(
        df_copy["signup_date"],
        format="%y-%m-%d",
        errors="coerce",
    )

    df_copy["signup_date"] = parsed_full_year.fillna(parsed_short_year)

    return df_copy



def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows.

    Args:
        df: DataFrame containing user data.

    Returns:
        DataFrame with duplicate rows removed.
    """
    df_cleaned = df.drop_duplicates(ignore_index=True)

    return df_cleaned



def remove_invalid_ages(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with invalid age values.

    Args:
        df: DataFrame containing dirty user data.

    Returns:
        DataFrame with rows containing invalid age values removed.
    """
    df_copy = df.copy()

    valid_age = (
        df_copy["age"].isna()
        | ((df_copy["age"] > 0) & (df_copy["age"] < 100))
    )

    df_copy = df_copy[valid_age]
    
    return df_copy


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing purchase amount, age, and status values.

    Args:
        df: DataFrame containing dirty user data.

    Returns:
        DataFrame with missing values processed.
    """
    df_copy = df.copy()

    df_copy = df_copy.replace(
        r"^\s*$",
        pd.NA,
        regex=True,
    )

    df_copy = df_copy.dropna(
        subset=["purchase_amount"]
    )

    df_copy["age"] = df_copy["age"].fillna(
        df_copy["age"].median()
    )

    df_copy["status"] = df_copy["status"].fillna(
        "Unknown"
    )

    return df_copy


def validate_cleaned_data(df: pd.DataFrame) -> None:
    """Check if the cleaning was completed correctly.

    Args:
        df: DataFrame containing user data.

    Raises:
        ValueError: If the cleaned data does not satisfy the validation rules.
    """
    if df.duplicated().any():
        raise ValueError("Duplicate rows remain.")

    if not pd.api.types.is_numeric_dtype(df["age"]):
        raise ValueError("age is not a numeric type.")

    if not pd.api.types.is_numeric_dtype(df["purchase_amount"]):
        raise ValueError("purchase_amount is not a numeric type.")
    
    if not pd.api.types.is_datetime64_any_dtype(df["signup_date"]):
        raise ValueError("signup_date is not a datetime type.")

    if df["purchase_amount"].isna().any():
        raise ValueError("Missing values remain in purchase_amount.")

    if df["age"].isna().any():
        raise ValueError("Missing values remain in age.")

    if df["status"].isna().any():
        raise ValueError("Missing values remain in status.")

    if df["signup_date"].isna().any():
        raise ValueError("Missing values remain in signup_date.")

    if ((df["age"] <= 0) | (df["age"] >= 100)).any():
        raise ValueError("Age values must satisfy 0 < age < 100.")

    if (df["name"] != df["name"].str.strip()).any():
        raise ValueError("name contains leading or trailing whitespace.")


def save_data(df: pd.DataFrame, output_path: Path) -> None:
    """
    """
    pass


def main() -> None:
    """
    """
    data_dir = Path(__file__).resolve().parent / "data"
    csv_path = data_dir / "dirty_users.csv"
    df = load_data(csv_path)
    validate_schema(df)


if __name__ == "__main__":
    main()
