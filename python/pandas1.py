import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])

# print(s)

# print('\n')
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s2)


data = {
  "Name": ["Sachin", "Virat", "Rohit"],
  "Runs": [100, 85, 95],
  'Balls': [120, 98, 110]
}

df = pd.DataFrame(data, index = [1, 2, 3])

print(df)

#output :
     Name  Runs  Balls
#1  Sachin   100    120
#2   Virat    85     98
#3   Rohit    95    110

#here 1, 2, 3 are known as labels. And rows are accessed based on this labels only 

#the loc method works on the basis of row labels and column labels,We use row labels to access the particular row, but if we specify the column label then we can access the particular data from the particular row for column label data only 



#https://onecompiler.com/python/43v7h7592


