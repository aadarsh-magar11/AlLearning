import matplotlib.pyplot as plt
import pandas as pd
datas=pd.read_csv("titanic.csv")
df=pd.DataFrame(datas)

datas=df.fillna({"survived":"0"})#filled survive

avg_age=df["age"].mean()
print(avg_age)
datas=df.fillna({"age":"30"})#filled the average age group for empty data



#survived
survived=len(df[df["survived"]==1])
surviveRate=(survived/len(df["survived"]))*100
print(f"the survival rate of titanic is {surviveRate:.2f}")
