# After loading the data set, to know about the rows we use : head(), tail()

import pandas as pd

print("The data set is:")
df = pd.read_csv("../sampleData.csv", index_col= False)
print(df)

#head()
#to read the top rows we use head(n), where it it will gives us the top n rows.
#if we won't give any n value then it automatically takes default value as n = 5.

#display top 5 rows
print(f"Top 5 rows are: \n{df.head(5)}")
# print(df.head()) #this wil also display the same answer as above


#display top 10 rows
print(f"Top 10 rows are: \n{df.head(10)}")




#tail()
#to read the last rows we use tail, syntax: dataframe.tail(n), if we give n then it prints the last n rows,
#if we won't give n then it will only prints last 5 rows

#display last 10 rows
print(f"Last 10 rows are: {df.tail(10)}")

#display last 5 rows
print(f"Last 10 rows are: {df.tail(5)}")
# print(f"Last 10 rows are: {df.tail()}") #it also prints the last 5 rows only just like the above
