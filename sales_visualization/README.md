# Sales Visualization Practice

## Overview

This script creates a figure containing two sales charts and saves the figure as a PNG image.

It loads sales log data from a CSV file, aggregates daily sales and total sales by category, creates a line chart and a bar chart, and saves the result to the `output` folder.

## What I practiced

* Loading CSV data with `pd.read_csv()`
* Parsing date columns with `parse_dates`
* Aggregating sales data with `groupby()` and `sum()`
* Sorting daily sales data by date
* Creating a figure with multiple charts using Matplotlib
* Creating a line chart and a bar chart using Seaborn
* Setting chart titles and axis labels
* Specifying file paths using the `pathlib` module
* Creating the destination directory with `mkdir(parents=True, exist_ok=True)`
* Saving a figure as a PNG image with `fig.savefig()`
* Separating the process into functions
* Using `if __name__ == "__main__"`

## What I learned

I learned how to create a figure containing multiple charts using Matplotlib.

By using Seaborn, I can create a line chart for daily sales trends and a bar chart for total sales by category.

I also learned how to save the figure I created as a PNG image.

Using `mkdir(parents=True, exist_ok=True)` makes it possible to create the destination folder automatically if it does not already exist.

Separating the process into functions made the script easier to read and maintain.

## Future improvements

* Add error handling when the CSV file does not exist
* Check whether required columns exist in the CSV file
* Export aggregated data to CSV files
* Add moving average lines to the daily sales chart
* Improve chart design, such as rotating date labels
* Save charts in multiple formats, such as PNG and PDF
