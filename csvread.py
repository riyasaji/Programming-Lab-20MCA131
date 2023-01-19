import csv

# Open the CSV file
with open('excelsheet.csv','r') as file:
    # Create a CSV reader
    reader=csv.reader(file)

    # Iterate over the rows of the CSV file
    for row in reader:
        # Print the rows as a list of strings
        print(row)