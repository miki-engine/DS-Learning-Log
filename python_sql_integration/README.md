# Python SQL Integration Practice

## Overview

This script integrates Python, Pandas, SQLite, and SQL to analyze e-commerce data.

It loads user, product, and order data from CSV files, stores each dataset as a table in a SQLite database, and executes an SQL query from Python to extract aggregated sales data for a specified product category.

## What I practiced

* Loading CSV data with `pd.read_csv()`
* Specifying file paths using the `pathlib` module
* Connecting to a SQLite database with `sqlite3.connect()`
* Creating or replacing database tables with `DataFrame.to_sql()`
* Joining tables with `INNER JOIN`
* Grouping data with `GROUP BY`
* Calculating aggregated values with `SUM()`
* Sorting aggregated results with `ORDER BY`
* Executing SQL queries with `pd.read_sql_query()`
* Passing query parameters with the `?` placeholder
* Using a `try` / `finally` block to ensure that the database connection is closed

## What I learned

I learned how to combine Python, Pandas, SQLite, and SQL in a single data analysis workflow. CSV data can be loaded into Pandas DataFrames, stored as SQLite tables, queried with SQL, and then returned to Python as another DataFrame.

I also learned that a `try` / `finally` block can ensure that `conn.close()` is executed even if an error occurs during database processing. This helps prevent database connections from being left open unexpectedly.

In addition, I learned how to parameterize SQL query values using placeholders. Instead of inserting a value directly into an SQL string, the `?` placeholder and the `params` argument can be used to pass the value separately from the SQL statement. This makes queries safer and helps prevent SQL injection when handling external values.

## Future improvements

* Separate database loading and query execution into reusable functions
* Add error handling for missing or invalid CSV files
* Practice executing multiple parameterized queries
* Practice using transactions with `commit()` and `rollback()`
* Extend the analysis by visualizing the SQL query results with Pandas and Matplotlib