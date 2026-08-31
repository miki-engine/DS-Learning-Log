from pathlib import Path
from typing import NamedTuple

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split


class SplitData(NamedTuple):
    """Represent divided data.

    Attributes:
        X_train: Feature data for model training.
        X_test: Feature data for model evaluation.
        y_train: Target data for model training.
        y_test: Target data for model evaluation.
    """
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series


DATA_DIR = Path(__file__).resolve().parent / "data"
CSV_PATH = DATA_DIR / "customer_behavior.csv"


FEATURE_COLUMNS = ["site_visits", "time_on_site", "email_opened"]
TARGET = "purchased"
TEST_SIZE = 0.2
RANDOM_SEED = 42


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
) -> SplitData:
    """Split the data into training and testing sets.

    Args:
        df: DataFrame containing customer behavior data.

    Returns:
        Split training and testing data.
    """
    X = df[FEATURE_COLUMNS]
    y = df[TARGET]

    split_data = SplitData(
        *train_test_split(
            X,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_SEED,
            stratify=y,
        )
    )

    return split_data


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
    """Predict class labels for the test data.

    Args:
        model: Trained logistic regression model.
        X_test: Feature data for model evaluation.

    Returns:
        Predicted labels.
    """
    y_pred = model.predict(X_test)

    return y_pred


def evaluate_model(
    y_test: pd.Series,
    y_pred: np.ndarray,
) -> tuple[float, np.ndarray]:
    """Evaluate the model using the test data.

    Args:
        y_test: Target data for model evaluation.
        y_pred: Predicted labels.

    Returns:
        Accuracy score and confusion matrix.
    """
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(
        y_test,
        y_pred,
        labels=[0, 1],
    )

    return accuracy, conf_matrix


def build_comparison_table(
    X_test: pd.DataFrame,
    y_test: pd.Series,
    y_pred: np.ndarray,
) -> pd.DataFrame:
    """Combine predicted labels with the test data.

    Args:
        X_test: Feature data for model evaluation.
        y_test: Actual target values for model evaluation.
        y_pred: Predicted class labels.

    Returns:
        DataFrame containing features, actual purchase labels,
        and predicted purchase labels.
    """
    result_df = X_test.copy()
    result_df["actual_purchase"] = y_test
    result_df["predicted_purchase"] = pd.Series(
        y_pred,
        index=result_df.index,
    )

    return result_df


def print_results(
    result_df: pd.DataFrame,
    accuracy: float,
    conf_matrix: np.ndarray,
) -> None:
    """Print results.

    Args:
        result_df: DataFrame containing features, actual purchase labels,
            and predicted purchase labels.
        accuracy: Accuracy score.
        conf_matrix: Confusion matrix.
    """
    print(result_df)
    print()
    print(f"Accuracy: {accuracy:.2%}")
    print()
    print("Confusion matrix:")
    print(conf_matrix)


def main() -> None:
    """Run the customer classification workflow."""
    df = load_data(CSV_PATH)
    split_data = prepare_data(df)
    model = train_model(
        split_data.X_train,
        split_data.y_train,
    )
    y_pred = predict_labels(
        model,
        split_data.X_test,
    )
    accuracy, conf_matrix = evaluate_model(
        split_data.y_test,
        y_pred,
    )
    result_df = build_comparison_table(
        split_data.X_test,
        split_data.y_test,
        y_pred,
    )
    print_results(result_df, accuracy, conf_matrix)


if __name__ == "__main__":
    main()
