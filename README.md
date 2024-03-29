# Mental Health Survey Analysis

This project analyzes data from a mental health survey. The data is stored in a CSV file named `Mental.csv`. The project uses Python and Matplotlib to visualize the distribution of various categorical variables in the dataset.

## Overview

The Python script loads the data from the CSV file and creates subplots to visualize the distribution of the following categorical variables:

- Gender
- Country
- Occupation
- Self Employed
- Family History
- Changes Habits

Each subplot displays the count of occurrences for each category within the variable.

## Code

```python
import csv
import matplotlib.pyplot as plt

# Function to load data from CSV file
def load_data(filename, column_index):
    # Implementation ...

# Function to create subplots
def create_subplot(ax, data, title, fontsize='medium'):
    # Implementation ...

# Main function
def main():
    # Loading data for each categorical variable
    # Implementation ...

    # Creating subplots for each categorical variable
    # Implementation ...

    # Setting titles and adjusting layout
    # Implementation ...

# Execute main function
if __name__ == "__main__":
    main()
