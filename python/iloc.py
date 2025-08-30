

import pandas as pd


data = {
    'Name': ['Sachin', 'Virat', 'Rohit'],
    'Runs': [100, 85, 95],
    'Balls': [120, 98, 110]
}



#iloc: it is used to access a row based on the index it is having by default it will have some index starts from (0 to length of the data set)
# unlike if we change the index also we can access the row based on index it is having by default(i.e.., which starts from 0 to length of the data set)

#*** iloc it is totally based on the default index it is having in both row and column
df = pd.DataFrame(data, index = ['a', 'b', 'c'])
print(df)

print(df.iloc[1])

#1. accessing with only row integer based 
#the output is : 
#Name     Virat
#Runs        85
#Balls       98
#Name: b, dtype: object

# ***here for virat data we given b as the index but in by default it has indexing starts from 0 which cannot be modified so we can access that virat through that default based index.


#2. accessing with both row and column integer based
print(df.iloc[1, 0] #1 is for row, and 0 is to access the column based on it's default index
#output :Virat

