# 1. using csv module to read and write csv files

import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile) # -> lets us read the csv file as a dictionary
    for row in reader:
        print(row)
        print(row['Name'], row['Age'], row['City'])

# writing dictionary to csv file
data_dict = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]

with open('data_dict.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader() # -> writes the header row
    writer.writerows(data_dict) # -> writes the data rows

# 2. using pandas to read and write csv files
import pandas as pd # type: ignore

dataFrames = pd.DataFrame([
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
])

dataFrames.to_csv('data_pandas.csv', index=False) # -> writes the dataframe to a csv file without the index

# reading the csv file using pandas
df = pd.read_csv('data_pandas.csv')
print(df)