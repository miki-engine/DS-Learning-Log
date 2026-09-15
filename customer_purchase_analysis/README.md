# Customer Purchase Analysis Practice

## Overview

This script analyzes the characteristics of users who make a purchase based on the provided customer web behavior data and visualizes the results.

It loads customer behavior data from a CSV file, calculates basic statistics and correlation coefficients between numerical variables, compares the average values between buyers and non-buyers, identifies variables that are strongly correlated with purchase status, and creates three visualizations: a heatmap, a scatter plot, and a box plot.

## What I practiced

* Loading CSV data with `pd.read_csv()`
* Specifying file paths using the `pathlib` module
* Separating the analysis process into functions
* Aggregating user data with `groupby()`
* Calculating correlation coefficients with `corr()`
* Sorting correlations by their absolute values
* Creating a heatmap, a scatter plot, and a box plot using Seaborn
* Creating the destination directory with `mkdir(parents=True, exist_ok=True)`
* Saving figures as PNG images with `fig.savefig()`
* Creating a `main()` function
* Using `if __name__ == "__main__"`

## What I learned

I learned how to calculate basic statistics and correlation coefficients from customer behavior data and use them to examine the characteristics of users who make a purchase.

I also learned how to compare buyers and non-buyers using grouped averages and how to visualize relationships between variables using heatmaps, scatter plots, and box plots.

## Future improvements

* Increase the amount of data
* Add error handling for cases where the CSV file does not exist
* Generate insights dynamically from the analysis results instead of hard-coding them