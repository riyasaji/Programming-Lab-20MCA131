import csv

# Specify the column indices that you want to raed
# e.g column 0 is the first column 1 is the second column , etc. .
columns_to_read=[0,2]

#open the csv file and read the contents
with open('data.csv','r') as f:
    clmn_reader=csv.reader(f)

    # Iterate over the rows of the CSV file
    for row in clmn_reader:
        # Print the contents of the specified columns
        print([row[i] for i in columns_to_read])