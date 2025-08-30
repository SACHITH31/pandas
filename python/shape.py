import pandas as pd

data = {
    'Name': ['Sachin', 'Virat', 'Rohit'],
    'Runs': [100, 85, 95],
    'Balls': [120, 98, 110],
    'State': ["India", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data, index = ['a', 'b', 'c'])

print(df)

#shape: it is used to say how many number of rows and columns for the given data set contains
print(df.shape)

#output: (3, 4) #3-rows, 4-columns
