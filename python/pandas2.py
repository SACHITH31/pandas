import pandas as pd

data = {
    'Name': ['Sachin', 'Virat', 'Rohit'],
    'Runs': [100, 85, 95],
    'Balls': [120, 98, 110]
}


df = pd.DataFrame(data, index = [1, 2, 3])

print(df)


#Accessing the rows
#Syntax: dataFrame.loc[row_label]


#accessing the particular row based on row labels
print(df.loc[1])

#accessing based on row labels + column labels
print(df.loc[1, "Name"])


#https://onecompiler.com/python/43v7hbhqp
