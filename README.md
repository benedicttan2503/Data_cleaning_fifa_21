# Data_cleaning_fifa_21
This project aims to clean and transform data in a CSV file named `fifa21_raw_data.csv`. The script provided performs various operations on the data to clean it and create a new CSV file named `fifa_clean_project.csv` with the cleaned data. The data is taken from this site: https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring?select=fifa21_raw_data.csv

## Process
1. The script imports the necessary libraries: `csv`, `math`, and `datetime`.
2. The script defines a list of new headers and their respective indices in the `new_headers` variable.
3. A list named `cleaned_data` is created to store the cleaned rows.
4. For each row in the CSV file, the following operations are performed to clean and transform the data:
   - The date string in column 17 is converted to a `datetime` object to extract the year, month, and day.
   - The height string in column 11 is split into feet and inches, converted to integers, and then converted to centimeters.
   - The weight string in column 12 is converted to an integer and from pounds to kilograms.
   - The value, wage, and release clause strings are processed to remove currency symbols and convert them to appropriate numerical values instead of shortcuts like M to represent Millions and K to represent thousand.
   - The team and contract information in column 9 is separated into individual variables.
   - The hits, weak foot, skill moves, and international reputation columns are cleaned and converted to integers.
   - The cleaned row is created by combining the original columns with the cleaned and transformed values.
   - The cleaned row is then appended to the `cleaned_data` list.
5. The script removes the old headers that are not needed in the cleaned data.
6. The new headers specified in the `new_headers` list are inserted at their respective indices in the header row.
7. The cleaned data rows are written to the output file using the `writerows()` function.

## Functionality

The provided code takes a raw FIFA 21 dataset (`fifa21_raw_data.csv`) and performs the following cleaning and transformation operations:

- Converts the date column from a string format to separate year, month, and day columns.
- Creates two seperate height columns; one for feet and inches and the other for centimeters.
- Converts the weight column from pounds to kilograms, creating two different weight columns.
- Cleans and converts the value, wage, and release clause columns from string format with shortcut characters like 'M' and 'K' to integer format.
- Separates the team and contract information into separate columns.
- Cleans and converts the hits, weak foot, skill moves, and international reputation columns to integers.
- Removes unnecessary columns from the dataset.
- Writes the cleaned and transformed data to a new CSV file named `fifa_clean_project.csv` with updated headers.
