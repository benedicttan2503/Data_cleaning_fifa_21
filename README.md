# Data_cleaning_fifa_21
This project aims to clean and transform data in a CSV file named `fifa21_raw_data.csv`. The script provided performs various operations on the data to clean it and create a new CSV file named `fifa_clean_project.csv` with the cleaned data.

## Process

1. The script imports the necessary libraries: `csv`, `math`, and `datetime`.
2. The script specifies the output file name as `fifa_clean_project.csv` by setting the `output` variable.
3. The script defines a list of new headers and their respective indices in the `new_headers` variable.
4. The script opens the original CSV file using the `csv.reader` object.
5. A list named `cleaned_data` is created to store the cleaned rows.
6. The script reads the header row from the CSV file using the `next()` function.
7. For each row in the CSV file, the following operations are performed to clean and transform the data:
   - The date string in column 17 is converted to a `datetime` object to extract the year, month, and day.
   - The height string in column 11 is split into feet and inches, converted to integers, and then converted to centimeters.
   - The weight string in column 12 is converted to pounds and then to kilograms.
   - The value, wage, and release clause strings are processed to remove currency symbols and convert them to appropriate numerical values.
   - The team and contract information in column 9 is separated into individual variables.
   - The hits, weak foot, skill moves, and international reputation columns are cleaned and converted to integers.
   - The cleaned row is created by combining the original columns with the cleaned and transformed values.
   - The cleaned row is appended to the `cleaned_data` list.
8. The script removes the old headers that are not needed in the cleaned data.
9. The new headers specified in the `new_headers` list are inserted at their respective indices in the header row.
10. The script opens the output file in write mode using `csv.writer` and writes the updated header row.
11. The cleaned data rows are written to the output file using the `writerows()` function.

## Functionality

The provided code takes a raw FIFA 21 dataset (`fifa21_raw_data.csv`) and performs the following cleaning and transformation operations:

- Converts the date column from a string format to separate year, month, and day columns.
- Converts the height column from feet and inches to centimeters.
- Converts the weight column from pounds to kilograms.
- Cleans and converts the value, wage, and release clause columns from string format to integer format.
- Separates the team and contract information into separate columns.
- Cleans and converts the hits, weak foot, skill moves, and international reputation columns to integers.
- Removes unnecessary columns from the dataset.
- Writes the cleaned and transformed data to a new CSV file named `fifa_clean_project.csv` with updated headers.

Please make sure to have the `fifa21_raw_data.csv` file in the same directory as the script file before running the code. The cleaned data will be stored in the `fifa_clean_project.csv` file.
