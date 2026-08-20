# User Data Cleaning Practice

## Overview

This script cleans dirty user data using Pandas.

It loads user data from a CSV file, validates the schema, standardizes name, purchase amount, and signup date formats, removes duplicate rows, handles missing values and invalid age values, validates the cleaned data, and saves the result as a CSV file.

This project uses a small dummy dataset for practice, so the purpose is to learn the basic workflow of data cleaning.

## What I practiced

* Loading CSV data with `pd.read_csv()`
* Specifying file paths using the `pathlib` module
* Validating required columns
* Raising `ValueError` when required columns are missing or cleaned data is invalid
* Removing leading and trailing whitespace with `.str.strip()`
* Converting values to a numeric type with `pd.to_numeric()`
* Removing unnecessary characters with `.str.replace()`
* Converting values to datetime type with `pd.to_datetime()`
* Handling multiple date formats
* Removing duplicate rows with `.drop_duplicates()`
* Removing rows with invalid age values
* Handling missing values with `dropna()` and `fillna()`
* Filling missing age values with the median
* Filling missing status values with `"Unknown"`
* Checking cleaned data with a validation function
* Saving cleaned data as a CSV file with `.to_csv()`
* Creating the destination directory with `mkdir(parents=True, exist_ok=True)`
* Separating the process into functions
* Creating a `main()` function
* Using `if __name__ == "__main__"`

## What I learned

I learned how to read dirty data from a CSV file, clean the data step by step, validate the cleaned result, and output it to a new CSV file.

I also learned that there is not one single absolute position for duplicate removal. The best position depends on what should be treated as a duplicate and whether earlier cleaning steps change the values.

In this script, I removed duplicates after standardizing names, purchase amounts, and signup dates. This makes it easier to detect rows that were originally written in different formats but became identical after cleaning.

I also learned that removing completely duplicate rows before missing-value handling can prevent duplicate records from affecting statistics such as the median.

By creating `validate_schema()` and `validate_cleaned_data()`, I learned how to check both the input data structure and the final cleaned result.

## Future improvements

* Add error handling when the CSV file does not exist
* Save removed or invalid rows to a separate CSV file
* Add a summary report showing how many rows were removed or modified
* Normalize `status` values if there are inconsistent labels
* Add unit tests for each cleaning function
* Make validation rules, such as the valid age range, configurable
