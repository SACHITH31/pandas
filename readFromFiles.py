import pandas as pd

#read from csv file
df = pd.read_csv("sampleData.csv", encoding="utf-8") #here encoding is not necessary and no only utf-8 but there is another that is "latin1"

#read from excel file 
# df = pd.read_excel("filename here")

#read from json file
# df = pd.read_json("filename here")

print(df)

