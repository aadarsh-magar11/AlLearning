import pandas as pd
data=pd.read_csv("pokemon.csv")
# data=data.drop(columns="Legendary")
# print(data)
# data=data.dropna(subset="Type2")
# data=data.fillna({"Type2":"None"})
# data["Type1"]=data["Type1"].replace({"Grass":"GRASS",
#                                      "Normal":"NORMAL",
#                                      "Bug":"BUG"})
# data["Name"] = data["Name"].str.lower()
data["Legendary"]=data["Legendary"].astype(bool)
print(data)
# data=data.drop_duplicates() to remove the duplicates if present