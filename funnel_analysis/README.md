# Funnel Analysis Practice

## Analysis Goal

Identify where users drop off in an e-commerce purchase funnel and examine differences in drop-off patterns across device types and traffic sources.

## Overview

This project analyzes e-commerce user behavior logs to identify bottlenecks in the purchase funnel and propose data-informed improvements.

The Python script imports CSV data into a SQLite database and uses SQL to count users who progress through funnel stages in chronological order. It then uses pandas to calculate overall conversion rates, step-to-step conversion rates, and drop-off rates.

The results are visualized using Matplotlib and Seaborn, saved as PNG images, and summarized in the console for both the overall funnel and individual segments.

For detailed methodology, findings, and limitations, see the [Analysis Report](analysis_report.md).

## What I Practiced

### Data Processing and SQL

- Loading CSV files into pandas DataFrames with `pd.read_csv()`
- Managing file paths using `pathlib`
- Creating and managing an SQLite database with `sqlite3`
- Storing DataFrames in database tables using `DataFrame.to_sql()`
- Joining user and event data with `INNER JOIN`
- Combining query results with `UNION ALL`
- Aggregating user counts using `GROUP BY` and `COUNT`
- Using CTEs to define sequential funnel stages
- Identifying the earliest qualifying event at each stage using `MIN(event_timestamp)` and chronological conditions
- Retrieving query results as DataFrames with `pd.read_sql_query()`
- Ensuring database connections are closed using `try` / `finally`

### Data Analysis and Visualization

- Calculating overall conversion rates, step-to-step conversion rates, and drop-off rates using pandas
- Comparing funnel performance across device types and traffic sources
- Identifying the stages with the largest absolute drop-offs and highest drop-off rates
- Creating funnel and drop-off bar charts using Matplotlib and Seaborn
- Configuring chart titles, axis labels, and percentage formatting
- Creating output directories and exporting figures as PNG images
- Interpreting results and proposing potential business improvements

### Refactoring and Code Quality

- Extracting shared SQL CTE definitions into a reusable constant to reduce duplication
- Configuring image export settings through optional keyword-only arguments
- Separating figure creation, image saving, and report output into functions
- Disabling interactive chart display while preserving PNG export and figure cleanup

## What I Learned

### SQL and Funnel Logic

Initially, I aggregated user counts at each funnel stage without checking the order of events. However, this approach could not confirm whether users had progressed through the funnel in the intended sequence.

To address this limitation, I revised the SQL queries to count users at each stage only when the corresponding event occurred after the previous stage. This helped me understand why chronological conditions are important when analyzing sequential user behavior.

### Interpreting Funnel Results

I learned that the stage with the largest number of lost users does not necessarily have the highest drop-off rate.

For example, in the Mobile segment, the largest absolute drop-off occurred between `view_item` and `add_to_cart`, while the highest drop-off rate occurred between `begin_checkout` and `purchase`.

This demonstrated the importance of considering both absolute user losses and relative drop-off rates when identifying bottlenecks and prioritizing potential improvements.

### Code Design and Maintainability

Initially, I defined the same funnel-stage CTEs separately in the overall and segment-level SQL queries.

After receiving feedback, I extracted the shared CTE definitions into a single constant and reused them in both queries. This reduced duplication while preserving the original analysis results.

Through this refactoring, I learned how separating shared logic from query-specific operations can make code easier to maintain and modify.

## Future Improvements

### Code Quality

- Centralize the names and order of the funnel stages
- Make funnel calculations less dependent on implicit row ordering
- Reduce duplicated logic in `main()`

### Data Validation and Testing

- Retain funnel stages with zero users in segment-level aggregation
- Strengthen input validation to handle missing values, invalid timestamps, and incomplete datasets
- Introduce automated tests with `pytest` to validate funnel calculations and chronological event conditions

### Further Analysis

- Test the statistical significance of differences in conversion rates and drop-off rates across segments
- Analyze funnel metrics across combinations of device and traffic_source to investigate potential confounding
- Add confidence intervals to express uncertainty in estimated conversion rates
- Estimate how much the number of Paid_Social purchasers could increase under hypothetical improvement scenarios
- For future A/B experiments, use power analysis to estimate the sample size required to detect meaningful improvements