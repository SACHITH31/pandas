import pandas as pd

#read from csv file
df = pd.read_csv("sampleData.csv", encoding="utf-8") 
#here encoding is not necessary and no only utf-8 but there is another that is "latin1"

#read from excel file 
# df = pd.read_excel("filename here")

#read from json file
# df = pd.read_json("filename here")

print(df)



'''

* to read a file which is in cloud then use this library "gcsfs".
* if any problems occured while reading a file change the encoding format either utf-8 or latin1.
* if any big set of data is given then it is best to read the data through loops.

'''