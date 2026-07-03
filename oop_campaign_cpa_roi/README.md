# Campaign class for ROI/CPA calculations practice

## Overview
This script creates campaign objects from master data, adds the sales amounts from conversion logs, and calculates CPA and ROI for each campaign.

## What I practiced
- Defining a Python class
- Creating instances from master data
- Managing objects with a dictionary
- Updating object attributes with methods
- Calculating CPA and ROI
- Ignoring invalid conversion data
- Using 'if __name__ == "__main__"'
- Writing a '.py' script instead of a Jupyter Notebook

## What I learned
I learned that a dictionary is useful for managing objects by ID.

In this script, I used 'campaign_id' as the dictionary key, so I could easily find the correct campaign object when processing each conversion log.

I also learned how to add calculation methods to a class. By defining 'calculate_cpa()' and 'calculate_roi()' inside the 'Campaign' class, each campaign object can calculate its own performance.

## Future improvements
- Handle conversion logs with unknown campaign IDs
- Split the main process into functions
- Load campaign master data and conversion logs from CSV files
- Export the summary result to a CSV file
- Add rounding rules for CPA and ROI