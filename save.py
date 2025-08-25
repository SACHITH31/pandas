import pandas as pd

data = [
    {
        "name": "sachith",
        "age": 18,
        "isShinobi": 'no',
    },
    
    {
        "name": "obito",
        "age": 32,
        "isShinobi": "yes",
    },
]
print(data)

#convert into dataFrame
df = pd.DataFrame(data)
print(df)


#convert this data into csv file
df.to_csv("saveCsv.csv") #now there will be indexing for every row(-) like 0, 1, 2 to remove this index we use indexing = False
# df.to_csv("saveCsv.csv", index= False)

#convert data into excel file
df.to_excel("saveExcel.xlsx")

#convert data into json file
df.to_json("saveJson.json")



'''
* while converting our own data into any other file format if by mistake if we wrote the wrong format like instead of "json" we write "jsonn" then it created a file with "jsonn" extenstion only. 
No error will shown. 
'''