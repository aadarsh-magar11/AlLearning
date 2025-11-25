import pandas as pd
datas=pd.read_csv("titanic.csv")
df=pd.DataFrame(datas)
new=df.fillna({"survived":"0"})
survived=len(df[df["survived"]==1])
surviveRate=(survived/len(df["survived"]))*100
print(f"the survival rate of titanic is {surviveRate:.2f}")
