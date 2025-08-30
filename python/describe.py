import pandas as pd

data = {
    'Name': ['Sachin', 'Virat', 'Rohit'],
    'Runs': [100, 85, 95],
    'Balls': [120, 98, 110],
    'State': ["India", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data, index = ['a', 'b', 'c'])

print(df)

print(df.describe())

#Output:

             Runs       Balls
count    3.000000    3.000000
mean    93.333333  109.333333
std      7.637626   11.015141
min     85.000000   98.000000
25%     90.000000  104.000000
50%     95.000000  110.000000
75%     97.500000  115.000000
max    100.000000  120.000000
