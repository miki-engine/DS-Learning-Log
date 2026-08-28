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
    conf_matrix = confusion_matrix(y_test, y_pred)

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


def main() -> None:
    """Run the customer classification workflow."""
    data_dir = Path(__file__).resolve().parent / "data"
    csv_path = data_dir / "customer_behavior.csv"
    df = load_data(csv_path)
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = train_model(X_train, y_train)
    y_pred = predict_labels(model, X_test)
    accuracy, conf_matrix = evaluate_model(y_test, y_pred)
    result_df = build_comparison_table(X_test, y_test, y_pred)

    print(result_df)
    print()

    print(f"Accuracy: {accuracy:.2%}")
    print()

    print("Confusion matrix:")
    print(conf_matrix)


if __name__ == "__main__":
    main()
