import pandas as pd

data=pd.read_csv('books.csv')
print(data.to_string())

#  .head() method returns the rows specified or only 5 rows from the top
print("\n\n")
print(data.head(),"\n")
print(data.head(7),"\n\n")

#data cleaning is another feature in pandas that allows cleaning bad data
'''bad datas means- empty cell, duplicate data, data in wrong format, worng data
'''

#cleaning empty cells
#this can be done using .dropna() method that returns a new dataframe with no empty cells
sample=pd.read_csv("sample.csv")
cleaned=sample.dropna()#this returns a new dataframe with no empty cells
print(cleaned.to_string())

'''
sample.dropna(inplace=True)
this above code makes change in the original data removing empty cells from it
'''

#  .fillna() method is used to fill the empty cells
filled=pd.read_csv("sample.csv")
#filled.fillna(150,inplace=True)#this filled all the empty spaces with 150 in the original data 
#print(filled.to_string())

#filling can be done specifically in one column only
'''
filled.fillna({"Date":"2025/10/12"},inplace=True)
filled.fillna({"Calories":400.4},inplace=True)
print(filled.to_string())
'''

#another best way to fill the data is by finding out the mean, median or mode
x=filled["Calories"].mean()# .median() or .mode()[0] can also be used to fill the spaces
filled.fillna({"Calories":x},inplace=True)
print(filled.to_string())

#converting the data into the desired form or format using pandas
naya=pd.read_csv("aarko.csv")
naya["Date"]=pd.to_datetime(naya["Date"], format='mixed')
naya.dropna(subset=["Date"],inplace=True)
print(naya.to_string())

