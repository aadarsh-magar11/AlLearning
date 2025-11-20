import pandas as pd 
data=pd.read_csv("pokemon.csv")

# tallpokemon=data[data["Height"]>=2]
# print(tallpokemon)

# heavy_pokemon=data[data["Weight"]>100]
# print(heavy_pokemon)
bug_pokemon=data[(data["Type1"] == "Bug") & (data["Type2"] == "Poison")]
print(bug_pokemon)