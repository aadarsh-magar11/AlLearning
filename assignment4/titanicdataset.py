import pandas as pd
data=pd.read_csv("titanic.csv")
df=pd.DataFrame(data)
total=df["name"].count()
print(f"the total number of people in titanic is {total}")
survived=df[df["survived"]==1]
print(survived.sum())