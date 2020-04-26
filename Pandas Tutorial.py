#Pandas Tutorial Practice

#Pandas Series
import pandas as pd
import numpy as np
series = pd.Series(data = [111, 222, 3], index = ['one','two','three'])
print(series)

#Creating Data frame from a series:
d = {'ColumnA' : pd.Series([111, 222, 333]),
         'ColumnB' : pd.Series([444, 555, 666])}

#Create the Dataframe
df = pd.DataFrame(d)

#Return the first row
data = df.iloc[0]

#Iterate over DataFrame Columns:
for column in df:
    print(column)

#Iterate over the items within the DataFrame:
for column,items in df.iteritems():
    print(column,items, sep = '\n')

#Iterate over rows within the dataframe:
for index_of_row, row in df.iterrows():
    print(index_of_row,row)

#Display each row as an object:
for row in df.itertuples():
    print(row)

#Sort by rows:
sorted_df = df.sort_index()

#Sort by columns
sorted_df = df.sort_values(by = 'columnA')

#Pandas Functionality
import pandas as pd

#Read Csv Files
df1 = pd.read_csv('mycsv.csv', index_col = ['ColumnA'])

#Read Excel FIles
df2 = pd.read_excel('myExcel.xlsx', index_col = ['ColumnA'])

#Read one excel sheet
df3 = pd.read_excel(open('myExcel.xlsx', 'rb'), sheet_name = 'sheet1')

#use head to return the first n records
r = df.head(10)

#Use tail to return the last n records
r = df.tail(10)

#Transpose:
transposed = df.T

#Shape of the dataset
new_shape = df.shape

#Quick Statistical Summary of a dataset using the describe method
df.describe()

#Table function; Apply our own function on all of the columns:
def myCustom(a,b):
    return a - b

df.pipe(myCustom, 1)

#Apply a function to all columnw:
def myCustom(a):
    return a - 1

df.apply(myCustom)

#Apply a function to each row:
df.apply(myCustom, axis = 1)

#Apply a function to each column
df.apply(myCustom, axis = 0)

#Data Engineering with pandas

#Check for missing value
df.notnull()

#Drop missing values
df.dropna()

#Filling missing values - Backward or forward filling
df.fillna()
df.fillna(method = 'backfill')
df.fillna(method = 'forward')


#Comparing Elements in percentage:
df.pct_change() #Column wise
df.pct_change(axis = 1) #row wise

#Compute the standard deviation of each column
df.std()

#Compute Correlation
df.corr()

#Aggregating Columns
df.aggregate({'ColumnName' : function})

#Grouping Row:
grouped_df = df.groupby('ColumnName')

#Grouping Multiple Columns
grouped_df = df.groupby(['ColumnA', 'ColumnB'])

#View Groups
grouped_df.groups

#Select a group
grouped_df.get_group(key)

#Filtering records
df.filter(myCustom) #myCustom takes in a parameter and returns a value

#Merging Functionalities
merged = pd.merge(left,right,left_on ='name', right_on = 'id', how = 'left')

#Union Data Frames
pd.concat([one,two])

#Compute Dates
pd.date_range(start, end)

#Plotting DataFrame

df.plot.bar() #Create a bar chart
df.diff.hist(bins = 10)
df.plot.scatter()