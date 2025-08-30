import pandas as pd

data = {
    "Name": ["Sachin", "Virat", "Rohit", "Dhoni", None],
    "Runs": [100, 85, None, 70, 90],       # None = missing value
    "Balls": [120, None, 110, 95, None],
    "Country": ["India", "India", None, "India", "India"]
}

df = pd.DataFrame(data)
print(df)

print('\n')

print(df.isnull().sum())

#output: 
Name       1
Runs       1
Balls      2
Country    1
dtype: int64
