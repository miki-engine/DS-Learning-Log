# Customer Classification Practice

## Overview

This script creates a logistic regression model to predict whether a customer will purchase or not.

It uses the number of site visits, time spent on the site, and whether the customer opened an email newsletter as features.

It loads customer behavior data from a CSV file, splits the data into training and test sets, trains a logistic regression model using the training data, predicts purchase labels using the test data, and compares the predicted labels with the actual purchase labels.

This project uses a small dummy dataset with about 100 records for practice, so the evaluation scores are only for learning purposes.

## What I practiced

* Loading CSV data with `pd.read_csv()`
* Splitting data with `train_test_split()`
* Using `stratify` when splitting classification data
* Separating features and target variables
* Training a logistic regression model using `sklearn.linear_model.LogisticRegression`
* Predicting class labels with `.predict()`
* Evaluating the model with `accuracy_score()` and `confusion_matrix()`
* Setting label order in a confusion matrix with `labels=[0, 1]`
* Building a comparison table using Pandas
* Using NumPy arrays returned by scikit-learn
* Defining constants for feature columns, target column, test size, and random seed
* Using `NamedTuple` to store split data
* Specifying file paths using the `pathlib` module
* Separating the process into functions
* Creating a `main()` function
* Using `if __name__ == "__main__"`

## What I learned

I learned how to create a basic classification workflow using scikit-learn.

In this script, I used `site_visits`, `time_on_site`, and `email_opened` as features, and `purchased` as the target variable. The features are stored in a DataFrame, the target variable is stored in a Series, and the predicted labels returned by scikit-learn are stored as a NumPy array.

I also learned that logistic regression can be used for binary classification. In this project, the model predicts whether each customer belongs to class `0` or class `1`.

The `train_test_split()` function returns four values: `X_train`, `X_test`, `y_train`, and `y_test`. Since using these values in the wrong order can cause bugs, I created a custom `NamedTuple` called `SplitData`. This made it possible to access the split data by name, such as `split_data.X_train` and `split_data.y_test`.

I learned how to use `stratify=y` when splitting classification data. This helps keep the class balance similar between the training data and the test data.

I also learned how to evaluate a classification model using accuracy and a confusion matrix. Accuracy shows the percentage of correct predictions, while a confusion matrix shows how the model classified each actual class.

Because this project uses a small dummy dataset, the evaluation results are not stable enough to judge the real performance of the model. However, they are useful for practicing the basic workflow of training, predicting, evaluating, and comparing classification results.

## Future improvements

* Increase the amount of training data
* Check whether required columns exist in the CSV file
* Add error handling when the CSV file does not exist
* Export the comparison table to a CSV file
* Add prediction probabilities with `.predict_proba()`
* Calculate additional metrics, such as precision, recall, and F1-score
* Try cross-validation with a larger dataset
* Compare logistic regression with other classification models
