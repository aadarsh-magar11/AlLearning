import pandas as pd

reading=pd.read_csv("aarko.csv")
reading.fillna({"Date":"'2020/12/22'"},inplace=True)
reading["Date"]=pd.to_datetime(reading["Date"],format="mixed")
for r in reading.index:
    if reading.loc[r,"Duration"]>60:
        reading.loc[r,"Duration"]=30
x=reading["Calories"].median()
reading.fillna({"Calories":x},inplace=True)
print(reading.to_string())

#duplicated datas can be removed using or .drop_duplicates() method
print(reading.duplicated())
reading.drop_duplicates(inplace=True)
print("\n after removing the duplicates")
print(reading.to_string())

#to find the correlation between the given data
print(reading.corr())