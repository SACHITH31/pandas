import pandas as pd

dataSet = {
    "Name": ["sachith", "ricky", "obito", "naruto", "hinata", "sasuke"],
    "Age": [1, 2, 3, 4, 5, 6],
    "Pin": [11, 22, 33, 44, 55, 66],
    "Country": ["india", "india", "konaha", "konaha", "konaha", "konaha"]
}

df = pd.DataFrame(dataSet)
print(df)

#FOR ACCESSING THE COLUMNS:
'''
To access a particular COLUMN there are two types to access a column those are:
1: df["Column_Name"]    #we use this type whenever we do some operation on only one column, and it return the particular column as "SERIES" format.
2: df[["Column_Name"]]  #we use this whenever we do some operations on more than one column, and it returns the data as in the form of "DATA FRAME" format.
'''

#now i want to operate some operation on only Name column so i use first method.
nameColumn = df["Name"]
print(f"The name column data is: \n{nameColumn}")

#now i want to access the multiple columns and perform some actions on them then we use second method.
setOfColumns = df[["Name", "Age"]]
print(f"The name and age columns data is: \n{setOfColumns}")