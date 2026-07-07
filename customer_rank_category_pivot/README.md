# Customer Rank Category Pivot Practice

## Overview

This script creates a cross-tab pivot table of sales amounts by customer rank and product category using Pandas.

It loads sales log data from a CSV file, summarizes the total sales amount for each rank and category, and displays the result as a pivot table.

## What I practiced

* Creating a cross-tab pivot table using Pandas
* Using `pd.pivot_table()`
* Setting index, columns, values, and aggregation function
* Filling missing combinations with 0
* Specifying file paths using the `pathlib` module
* Loading CSV data with `pd.read_csv()`
* Using `if __name__ == "__main__"`
* Writing a `.py` script instead of a Jupyter Notebook

## What I learned

I learned how to create a cross-tab pivot table using Pandas.

By using `rank` as the index and `category` as the columns, I can summarize sales amounts in a table that is easier to compare.

I also learned how to specify file paths using the `pathlib` module. This makes it easier to read files from a folder relative to the script location.

## Future improvements

* Add error handling when the CSV file does not exist
* Check whether required columns exist in the CSV file
* Export the pivot table result to a CSV file
* Add more aggregation options, such as count and average
* Sort ranks and categories in a specific order
