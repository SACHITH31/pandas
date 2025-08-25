import pandas as pd

dataSet = {
    "Name": ["sachith", "ricky", "obito", "naruto", "hinata", "sasuke"],
    "Age": [1, 2, 3, 4, 5, 6],
    "Pin": [11, 22, 33, 44, 55, 66],
    "Country": ["india", "india", "konaha", "konaha", "konaha", "konaha"]
}

df = pd.DataFrame(dataSet)
print(df)

#ACCESSING THE ROWS