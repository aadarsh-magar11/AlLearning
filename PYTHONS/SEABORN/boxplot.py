import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset("penguins")
# sns.boxplot(data=data,x="species", y="body_mass_g",hue="island")
# plt.show()

#violin plot - same as box-whiskerplot but in same like that of a violin
'''
the end of whiskers inside the plot shows the maximum and minimum points
the ends of the box inside shows the first and third quartile
the middle part of the box represents median of the data
'''
# sns.violinplot(data=data, x="species", y="body_mass_g",palette=["yellow"])
# sns.swarmplot(data=data, x="species", y="body_mass_g",hue="sex",size=3, palette=["blue","orange"])


#kernal density plot or kdeplot- plot that shows the density within the data, histogram in different mannner
sns.kdeplot(data=data, x="body_mass_g", hue="island", fill=True)
plt.show()
