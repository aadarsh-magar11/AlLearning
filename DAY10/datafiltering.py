import pandas as pd
 
data=pd.read_csv("pokemon.csv")
# .mean() is used to print the mean of the data
# print(data.mean(numeric_only=True))
# print(data.min(numeric_only=True))
# print(data.max(numeric_only=True))
# print(data.sum(numeric_only=True))
# print(data.count())

# print(data["Height"].mean())
# print(data["Weight"].max())
# print(data["Height"].min())
# print(data["Weight"].sum())
# print(data["Type2"].count())

#grouping can be done in python using .groupby()
group=data.groupby("Type1")
# print(group["Height"].mean())
print(group["Weight"].max())
# print(group["Height"].min())