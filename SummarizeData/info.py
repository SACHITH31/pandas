import pandas as pd

df = pd.read_csv('../sampleData.csv')
print(df.info())

'''
The output is:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21 entries, 0 to 20              #this says the number of rows in our data set.
Data columns (total 5 columns):              #this says the number of columns in our data set. 
 #   Column      Non-Null Count  Dtype   
---  ------      --------------  -----
 0   ID          21 non-null     int64        #here not null means "no value is missing in the data set".
 1   Name        21 non-null     object       #here object specifies it is a string, dates, lists, dictonares. 
 2   Age         21 non-null     int64
 3   Department  21 non-null     object
 4   Salary      21 non-null     int64
dtypes: int64(3), object(2)                  
memory usage: 972.0+ bytes
None

'''