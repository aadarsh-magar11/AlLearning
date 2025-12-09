import pandas as pd
data={
    "name":["ram", "shyam", "sita", "gita"],
    "roll no.":[1,2,3,4]
}
df = pd.DataFrame(data)
df["age"]=[19,20,20,21]
print(df)

new_row=pd.DataFrame([{"name":"hari","roll no.":5, "age":19}])
df=pd.concat([df,new_row])
print(df)  

df=pd.read_csv("pokemon.csv", index_col="Name")
# print(df["Name"])
# print(df[["Name","Height","Weight"]].to_string())
# print(df.loc[0])
# print(df)
# print(df.loc["Pikachu"])
pokemon = input("enter the name of the pokemon to search:")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")