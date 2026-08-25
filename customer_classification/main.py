from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split


def load_data(csv_path: Path) -> pd.DataFrame:
    """Load customer behavior logs CSV file into DataFrame.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        DataFrame containing customer behavior data.
    """
    df = pd.read_csv(csv_path)

    return df


def prepare_data(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split the data into training and testing sets.

    Args:
        df: DataFrame containing customer behavior data.

    Returns:
        Training features, testing features, training target, and testing target.
    """
    X = df[["site_visits", "time_on_site", "email_opened"]]
    y = df["purchased"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    return X_train, X_test, y_train, y_test


def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> LogisticRegression:
    """Train a logistic regression model.

    Args:
        X_train: Feature data for model training.
        y_train: Target data for model training.

    Returns:
        Trained logistic regression model.
    """
    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model


def predict_labels(
    model: LogisticRegression,
    X_test: pd.DataFrame,
) -> np.ndarray:
    """
    """
    pass


def evaluate_model(
    y_test: pd.Series,
    y_pred: np.ndarray,
) -> tuple[float, np.ndarray]:
    """
    """
    pass


def build_comparison_table(
    X_test: pd.DataFrame,
    y_test: pd.Series,
    y_pred: np.ndarray,
) -> pd.DataFrame:
    """
    """
    pass


def main() -> None:
    """
    """
    pass


if __name__ == "__main__":
    main()