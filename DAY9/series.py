import pandas as pd

alist=[100, 101, 102, 103, 200, 202, 303]
series=pd.Series(alist) #index=["a","b",........] can be used to custom the indexing
print(series)

print(series[series>150])
# .loc can be used to access the value of a location

#for dictionaries
calories={"day 1":2000, "day 2":2200, "day 3": 2100, "day 4":2500, "day 5":2300}
anotherseries=pd.Series(calories)
print(anotherseries)


pokemon=["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmelon", "Charizard"]
poke=pd.Series(pokemon, index=[1,2,3,4,5,6])
print(poke)