import pandas as pd     # Pandas means Python for Data Analysis/Panel Data

# Reading the csv file
data=pd.read_csv("sample.csv")

# Printing first 5 rows of the data
print(data.head())

#Printing last 5 rows of data
print(data.tail())

print(data.shape)

#Printing data types of each column
print(data.dtypes)

# Gives all the info about data(column names, data types, number of non-null rows)
print(data.info())

# Describes Count of records, Mean, Standard Deviation, Minimum and Maximum values
print(data.describe())

# Defines null rows in the table
print(data.isnull())

# Deleting null rows
data.dropna(inplace=True) # Deletes all the null rows in the dataset
# new_data=data.dropna()  # Returns a new dataset by deleting the null rows
print(data)

# Replacing null values
data.fillna(490,inplace=True) # Replaces null values of all the columns
data.fillna({'Price (USD)':490},inplace=True) # Replaces null values of the specified column
print(data)

# # Accessing records using indexing
print(data.loc[2])
print(data.iloc[3])