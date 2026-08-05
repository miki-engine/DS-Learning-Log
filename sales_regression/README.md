# Sales Regression Practice

## Overview

This script creates a linear regression model to predict sales from advertising costs and coupon values.

It loads marketing sales data from a CSV file, splits the data into training and test sets, trains a linear regression model using the training data, predicts sales using the test data, and compares the predicted values with the actual sales values.

This project uses a small dummy dataset for practice, so the evaluation scores are only for learning purposes.

## What I practiced

* Loading CSV data with `pd.read_csv()`
* Splitting data with `train_test_split()`
* Separating features and target variables
* Training a linear regression model using `sklearn.linear_model.LinearRegression`
* Predicting sales with `.predict()`
* Evaluating the model with `mean_absolute_error()` and `r2_score()`
* Building a comparison table using Pandas
* Calculating prediction errors and absolute errors
* Using NumPy arrays returned by scikit-learn
* Specifying file paths using the `pathlib` module
* Separating the process into functions
* Creating a `main()` function
* Using `if __name__ == "__main__"`

## What I learned

I learned how to create a basic machine learning workflow using scikit-learn.

In this script, I used `advertising_cost` and `coupon_value` as features, and `sales` as the target variable. The features are stored in a DataFrame, the target variable is stored in a Series, and the predicted values returned by scikit-learn are stored as a NumPy array.

I also learned why it is important to split data into training and test sets. If a model is trained and evaluated using the same data, the evaluation result may be too optimistic. By setting aside part of the data for testing, I can check how well the model performs on data it has not seen during training.

MAE, or mean absolute error, is the average of the absolute differences between the predicted values and the actual values. A smaller MAE means the predictions are closer to the actual values.

R-squared is a metric that shows how well the model explains the variation in the actual data. A higher R-squared score usually means the model explains the data better, but it can become negative when the model performs poorly on test data.

Because this project uses only a small dummy dataset, the MAE and R-squared scores are not stable enough to judge the real performance of the model. However, they are useful for practicing the basic workflow of training, predicting, evaluating, and comparing results.

## Future improvements

* Increase the amount of training data
* Add more features that may affect sales
* Check whether required columns exist in the CSV file
* Add error handling when the CSV file does not exist
* Export the comparison table to a CSV file
* Visualize actual sales and predicted sales
* Try cross-validation with a larger dataset
* Compare the linear regression model with other regression models
