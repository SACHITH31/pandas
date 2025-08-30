import pandas as pd

data = {
    'Name': ['Sachin', 'Virat', 'Rohit'],
    'Runs': [100, 85, 95],
    'Balls': [120, 98, 110],
    'State': ["India", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data, index = ['a', 'b', 'c'])

print(df)

#columns: this method is used to show what are the columns a data set contains
print(df.columns)

#output: Index(['Name', 'Runs', 'Balls', 'State'], dtype='object')
