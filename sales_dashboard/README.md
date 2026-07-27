# Sales Dashboard Practice

## Overview

This script creates an interactive sales dashboard using Streamlit.

It loads sales log data from a CSV file, allows the user to select product categories from the sidebar, filters the DataFrame based on the selected categories, and displays both the filtered data and a daily sales trend chart.

## What I practiced

* Creating an interactive dashboard using Streamlit
* Loading CSV data with `pd.read_csv()`
* Parsing date columns with `parse_dates`
* Caching loaded data with `@st.cache_data`
* Creating sidebar filters with `st.sidebar.multiselect()`
* Filtering a DataFrame by category with `.isin()`
* Getting unique category values with `dropna()`, `unique()`, and `tolist()`
* Aggregating sales data with `groupby()` and `sum()`
* Sorting sales data by date and category
* Creating a line chart using Seaborn
* Setting chart titles and axis labels
* Displaying a DataFrame with `st.dataframe()`
* Displaying a Matplotlib figure with `st.pyplot()`
* Showing a message with `st.info()`
* Stopping the app safely with `st.stop()`
* Specifying file paths using the `pathlib` module
* Separating the process into functions
* Preventing memory leaks with `plt.close()`

## What I learned

I learned how to create a simple interactive dashboard using Streamlit.

By using `st.sidebar.multiselect()`, I can let the user choose which categories to display. The DataFrame and chart are updated based on the selected categories.

I also learned how to use `@st.cache_data` to cache loaded CSV data. This can make the app more efficient because the data does not need to be loaded again every time the screen updates.

By using Seaborn with `hue="category"`, I can compare daily sales trends for multiple categories in a single line chart.

I also learned how to safely stop the app with `st.stop()` and show a helpful message with `st.info()` when no categories are selected.

## Future improvements

* Add a date range filter
* Add summary metrics, such as total sales and average sales
* Add a category ranking chart
* Allow users to download the filtered data as a CSV file
* Check whether required columns exist in the CSV file
* Add error handling when the CSV file does not exist
* Improve the chart design, such as rotating date labels
* Deploy the dashboard so it can be viewed outside my local environment
