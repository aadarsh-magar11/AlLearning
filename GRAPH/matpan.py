import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("pokemon.csv")
type_count=df["Type1"].value_counts()
plt.barh(type_count.index, type_count.values)
plt.title("number of pokemon by type")
plt.xlabel("number of pokemon")
plt.ylabel("type of pokemon")
plt.show()