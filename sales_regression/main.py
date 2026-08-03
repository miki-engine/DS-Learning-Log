from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def load_data(csv_path: Path) -> pd.DataFrame:
    """Load marketing sales logs CSV file into DataFrame.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        DataFrame containing marketing sales data.
    """
    df = pd.read_csv(csv_path)

    return df


def prepare_data(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split the data into training and testing sets.

    Args:
        df: DataFrame containing marketing sales data.

    Returns:
        Training features, testing features, training target, and testing target.
    """
    X = df[["advertising_cost", "coupon_value"]]
    y = df["sales"]

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
) -> LinearRegression:
    """Train a linear regression model.

    Args:
        X_train: Feature data for model training.
        y_train: Target data for model training.

    Returns:
        Trained linear regression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model


def evaluate_model(
    model: LinearRegression,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> tuple[np.ndarray, float, float]:
    """Predict sales and evaluate the model using the test data.

    Args:
        model: Trained linear regression model.
        X_test: Feature data for model evaluation.
        y_test: Actual target values for model evaluation.

    Returns:
        Predicted values, mean absolute error, and R-squared score.
    """
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return y_pred, mae, r2


def build_comparison_table(
    X_test: pd.DataFrame,
    y_test: pd.Series,
    y_pred: np.ndarray,
) -> pd.DataFrame:
    """Combine the predicted results with the test data.

    Args:
        X_test: Feature data for model evaluation.
        y_test: Actual target values for model evaluation.
        y_pred: Predicted values.

    Returns:
        DataFrame containing features, actual sales, predicted sales,
        errors, and absolute errors.
    """
    result_df = X_test.copy()
    result_df["actual_sales"] = y_test
    result_df["predicted_sales"] = pd.Series(y_pred, index=result_df.index)
    result_df["error"] = result_df["predicted_sales"] - result_df["actual_sales"]
    result_df["absolute_error"] = result_df["error"].abs()

    return result_df


def main() -> None:
    """Run the sales regression workflow."""
    data_dir = Path(__file__).resolve().parent / "data"
    csv_path = data_dir / "marketing_sales.csv"
    df = load_data(csv_path)
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = train_model(X_train, y_train)
    y_pred, mae, r2 = evaluate_model(model, X_test, y_test)

    print(f"Mean absolute error: {mae:.2f}")
    print(f"R-squared score: {r2:.3f}")



if __name__ == "__main__":
    main()