# A/B Test Analysis Practice

## Overview

This project analyzes an A/B test comparing the purchase rates of an existing design (Control) and a new design (Test).

The script loads CSV data into a SQLite database, aggregates user-level purchase data using SQL, calculates purchase rates with pandas, and performs a one-sided two-proportion z-test to evaluate whether the new design improves the purchase rate.

The analysis report includes statistical results, an assessment of practical significance, and business recommendations.

## What I Practiced

### Data Processing and SQL

- Loading CSV files into pandas DataFrames using `pd.read_csv()`
- Managing file paths with `pathlib`
- Creating and managing an SQLite database using `sqlite3`
- Saving DataFrames as database tables with `DataFrame.to_sql()`
- Combining tables using `INNER JOIN`
- Aggregating data with `GROUP BY`, `COUNT(DISTINCT ...)`, and `CASE WHEN`
- Retrieving SQL query results as DataFrames using `pd.read_sql_query()`
- Using `try` / `finally` to ensure that database connections are closed
- Selecting rows by group labels using `set_index()` and `.loc[]`

### Statistical Analysis

- Calculating purchase rates for the Control and Test groups
- Performing a one-sided two-proportion z-test using `proportions_ztest()`
- Interpreting z-statistics, p-values, and statistical significance
- Calculating absolute differences and relative changes in purchase rates
- Translating statistical results into practical considerations and business recommendations

### Error Handling and Testing

- Preventing division by zero when the Control group's purchase rate is zero
- Raising `ValueError` when the z-test cannot be calculated because all users have the same purchase outcome
- Organizing multiple test scenarios in a dictionary
- Using `try` / `except` / `else` to verify expected exceptions
- Manually checking report output across seven test scenarios

## Results and Interpretation

The observed purchase rates were:

| Metric | Result |
|---|---:|
| Control purchase rate | 7.36% |
| Test purchase rate | 8.65% |
| Absolute difference | +1.30 percentage points |
| Relative change | +17.62% |
| Z-statistic | 0.7553 |
| p-value | 0.2250 |
| Significance level | 0.05 |

Although the Test group had a higher observed purchase rate, the result was not statistically significant at the 5% significance level.

Therefore, the analysis does not provide sufficient evidence that the new design improves the purchase rate. Its practical value also remains uncertain because the implementation costs and expected financial benefits are unknown.

## What I Learned

### Understanding Hypothesis Testing

A one-sided two-proportion z-test can be used to evaluate whether one population proportion is higher than another.

In this analysis, the hypotheses were:

- **Null hypothesis (H0):** The Test group's purchase rate is less than or equal to the Control group's purchase rate.
- **Alternative hypothesis (H1):** The Test group's purchase rate is higher than the Control group's purchase rate.

I learned that a p-value is not the probability that the null hypothesis is true. Instead, under the null hypothesis, it represents the probability of obtaining a test statistic at least as extreme as the observed one in the direction specified by the alternative hypothesis.

A non-significant result means that there is insufficient evidence to reject the null hypothesis. It does not prove that the null hypothesis is true or that the two purchase rates are equal.

### Statistical vs. Practical Significance

Statistical significance and practical significance address different questions.

Statistical significance concerns the strength of evidence against the null hypothesis, whereas practical significance concerns whether an observed effect is meaningful in a real-world context.

Even a statistically significant improvement may not justify implementing a new design if the expected benefits do not outweigh the costs.

I also learned to distinguish between two ways of expressing changes in purchase rates:

- **Absolute difference:** The difference between two rates, expressed in percentage points.
- **Relative change:** The percentage change relative to the Control group's rate.

### Data Validation and Reliable Analysis

A program that runs without errors does not necessarily produce reliable results.

Before joining tables, it is important to check the consistency of the data, including whether user IDs are duplicated or missing from either dataset.

Error handling is also important when processing unexpected inputs. In particular, division by zero and undefined statistical calculations should be handled explicitly rather than silently producing misleading results.

Testing multiple scenarios helped me understand the importance of checking both normal behavior and expected failures.

## Additional Notes

### SQL Identifiers and Reserved Words

I initially misunderstood when SQL identifiers needed to be enclosed in double quotes.

I learned that identifiers conflicting with SQL reserved words should be quoted. For example, `"group"` must be quoted when used as a column name because `GROUP` is a SQL keyword.

### Choosing the Appropriate JOIN

`INNER JOIN` includes only rows that satisfy the join condition in both tables.

Even if the SQL query is correct, unmatched user IDs can affect the aggregation results by excluding records from the analysis.

Therefore, I should verify the relationship between datasets before joining them and select the appropriate type of JOIN based on the analysis requirements.

### Designing Additional A/B Tests

When an A/B test does not provide sufficient evidence of improvement, simply continuing to collect data until the result becomes significant is not an appropriate testing strategy.

Before conducting a follow-up experiment, it is important to define a meaningful target effect, determine the required sample size through power analysis, and establish the testing procedure in advance.

## Future Improvements

- Automate test validation using `pytest`
- Implement power analysis to estimate the required sample size
- Add confidence intervals to communicate uncertainty in the estimated effect
- Extend input validation to handle additional invalid or incomplete datasets