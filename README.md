# Sales Data Cleaner and Grouping Tool

## Overview

The Sales Data Cleaner and Grouping Tool is a project designed to efficiently manage and organize raw POS (Point of Sale) sales data. Its primary objectives are to clean the raw data, group sales data based on SKUs (Stock Keeping Units), and optimize storage usage within Salesforce. By grouping sales data, it reduces the number of individual entries, making data management more streamlined and efficient.

## Features

- **Data Cleaning**: The tool cleans raw POS sales data to ensure consistency and accuracy.
- **Data Grouping**: Sales data is grouped based on SKUs, reducing the number of entries and optimizing storage usage.
- **Reference Master Excel File**: The project references a master Excel file containing a list of SKUs and their corresponding categories (category, subcategory, micro category). This reference is crucial for organizing and categorizing the sales data accurately.
- **Unique Identification**: Each sales data entry is assigned a unique abbreviation based on the reference master Excel file. This abbreviation is later used to create a unique sales data ID.
- **Category Information**: The reference master Excel file also includes official category, subcategory, and micro category names, providing comprehensive information for data analysis.
- **Date Filtering**: The tool includes functionality to filter data based on month and year, enabling users to analyze sales data for specific time periods.

## Usage

1. **Input Raw Sales Data**: Provide the raw POS sales data to the tool.
2. **Clean Data**: Execute the data cleaning process to ensure data consistency.
3. **Group Data**: Utilize the grouping functionality to group sales data based on SKUs.
4. **Reference Master Excel File**: Ensure the master Excel file containing SKU information is accessible and up-to-date.
5. **Generate Unique IDs**: The tool automatically generates unique sales data IDs based on the reference master Excel file.
6. **Analyze Data**: Use the categorized and grouped sales data for analysis, reporting, and decision-making.

## Requirements

- Python 3.x
- Pandas library
- Excel file containing the reference master data

## Installation

1. Clone the repository: `git clone https://github.com/elHakerDeCarolSteeam/Data_Maintenance.git`
2. Install dependencies: `pip install pandas`

## Configuration

1. Update the file paths in the configuration file to point to the location of the raw sales data and the reference master Excel file.

## Contributors

- Bryan Chacha Gonzalez(https://github.com/elHakerDeCarolSteeam)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the need for efficient data management in Salesforce.
- Built with Python and the Pandas library.

## Screenshots 
![Github_Screenshots_part1](https://github.com/elHakerDeCarolSteeam/Data_Maintenance/assets/161890147/ad6dc2c8-d9d5-4949-96e0-488c41b8fed1)


