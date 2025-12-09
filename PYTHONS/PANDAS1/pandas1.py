'''
pandas is a library in python that allows in cleaning and managing the data

Pandas gives you answers about the data. Like:
Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?

'''
import pandas as pd
print(pd.__version__)


raw_data={
    'roll':[1,2,3],
    'name':["ram","shyam","hari"]
}
# .DataFrame(....) manages the data in tabular form
daataa=pd.DataFrame(raw_data)
print(daataa)

#Series in pandas is like column in a table
a=[21,32,44]
num=pd.Series(a)
print(num)
label=pd.Series(a,index=["x","y","z"])#labels can be created as wished
print(label)


day={"sunday":"push","monday":"pull","tuesday":"leg"}
routine=pd.Series(day)
print(routine,"\n")
 
routine=pd.Series(day,index=["sunday"])
print(routine,"\n")

#DataFrames 
menu={
    'food':['chicken-momo','chowmein','lollipop'],
    'price':[150,100,100]
}
show=pd.DataFrame(menu,index=[1,2,3])
print(show)

print(show.loc[2])

#reading a csv using DataFrame
user=pd.read_csv('books.csv')
print(user.to_string())#this reads all the content of the csv file

#to find the maximum number of rows one's system can display
print(pd.options.display.max_rows)

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 
#dataframe displays in rows where series displays in column


