import pandas as pd

data = {
    'Name': ['Sachin', 'Virat', 'Rohit'],
    'Runs': [100, 85, 95],
    'Balls': [120, 98, 110],
    'State': ["India", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data, index = ['a', 'b', 'c'])

print(df)

#info : it is used to get the total information about the data set.like is the data set containing any null values, how much memory it is occupied, what are the data types each column is storing, and etc..,
print(df.info())


#output:
<class 'pandas.core.frame.DataFrame'>
Index: 3 entries, a to c
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    3 non-null      object
 1   Runs    3 non-null      int64 
 2   Balls   3 non-null      int64 
 3   State   3 non-null      object
dtypes: int64(2), object(2)
memory usage: 120.0+ bytes
None
