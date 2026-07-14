# Membership Sales Merge Analysis

## Overview

This script analyzes total purchase amounts by membership rank using Pandas.

It loads user master data and purchase log data from two CSV files, merges them using `user_id` as the key, and aggregates total sales by membership rank.

## What I Practiced

* Specifying file paths using the `pathlib` module
* Loading CSV data with `pd.read_csv()`
* Separating the process into functions
* Merging user master data and purchase logs using `pd.merge()`
* Using type hints with Pandas DataFrames
* Using `if __name__ == "__main__"`
* Writing a `.py` script instead of a Jupyter Notebook

## What I learned

I learned how to merge user master data with purchase logs on `user_id`.

By using `pd.merge()`, I can combine information from different tables and analyze the data more easily.

I also learned how to use groupby() to aggregate total purchase amounts by membership rank.

Separating the process into functions made the script easier to read and understand.

## Future improvements

* Add error handling when the CSV file does not exist
* Check whether required columns exist in each CSV file
* Handle purchase logs with unknown `user_id`
* Export the result to a CSV file
* Add more aggregation metrics, such as purchase count and average purchase amount