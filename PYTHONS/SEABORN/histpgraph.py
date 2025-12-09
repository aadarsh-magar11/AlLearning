import seaborn as sns
import matplotlib.pyplot as plt
penguin=sns.load_dataset("penguins")
# print(penguin)
sns.histplot(data=penguin, x="body_mass_g",
             hue="sex",
             multiple="stack")
plt.show()