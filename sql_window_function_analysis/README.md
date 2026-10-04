# SQL Window Function Practice

## Overview

This project contains four SQL window function exercises using monthly revenue data by category.

The exercises cover ranking values within groups, calculating cumulative totals, comparing values with the previous month, and extracting the highest value from each category.

## What I practiced

* Using window functions with `OVER()`
* Dividing rows into groups with `PARTITION BY`
* Ranking data with `RANK()`
* Calculating cumulative totals with `SUM()`
* Retrieving the previous row's value with `LAG()`
* Calculating differences between the current and previous month's revenue
* Combining window functions with CTEs
* Sorting query results with `ORDER BY`

## What I learned

Window functions allow calculations such as ranking, cumulative totals, and comparisons with previous rows while preserving the original row structure. Unlike `GROUP BY`, window functions do not combine multiple rows into a single aggregated row.

I also learned that `ORDER BY` inside the `OVER()` clause and the final `ORDER BY` clause have different purposes.

The `ORDER BY` inside `OVER()` defines the order of rows used by the window function. For example, it determines the ranking order for `RANK()`, the calculation order for a cumulative `SUM()`, or which row is considered the previous row for `LAG()`.

The final `ORDER BY` determines the order in which the rows are displayed in the query result. It does not determine how the window function performs its calculation.

Window functions generally cannot be used directly in a `WHERE` clause because filtering with `WHERE` occurs before window functions are evaluated. A CTE or subquery can be used as an additional query layer, allowing the window function result to be filtered afterward.

## Future improvements

* Practice using `ROW_NUMBER()` and `DENSE_RANK()` and understand how they differ from `RANK()`
* Practice using `LEAD()` to compare values with the following row
* Practice specifying window frames with `ROWS BETWEEN`
* Practice combining multiple window functions in a single query