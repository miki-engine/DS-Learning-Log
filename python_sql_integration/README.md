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

## Additional notes

I initially misunderstood how SQL placeholders work. I learned that placeholders can be used for values, but not directly for table names or column names because those are part of the SQL structure itself.

Without a `try` / `finally` block, an unhandled error can prevent the code after the error from being executed, including `conn.close()`. As a result, the database connection may remain open longer than intended. If an active transaction is holding a database lock at that time, the lock may also remain until the transaction is rolled back, the connection is closed, or the process ends.

I also initially misunderstood what is being locked. The database connection itself is not what is locked. SQLite uses locking to control access to the database, and only one connection can perform a write transaction at a time. Other write operations may need to wait until the current writer finishes.

## Future improvements

* Separate database loading and query execution into reusable functions
* Add error handling for missing or invalid CSV files
* Practice executing multiple parameterized queries
* Practice using transactions with `commit()` and `rollback()`
* Extend the analysis by visualizing the SQL query results with Pandas and Matplotlib