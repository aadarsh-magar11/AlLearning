import seaborn as sns
import matplotlib.pyplot as plt
# sns.set_context("notebook")
sns.set_style("whitegrid")
tips=sns.load_dataset("tips")#importing the readily available data sets of seaborn
print(tips)
print(tips["sex"].value_counts())
print(tips["smoker"].value_counts())
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex",
                palette="Dark2")
sns.despine()
sns.stripplot(data=tips,x="sex",y="tip",
                hue="day",)
sns.swarmplot(data=tips, x="sex",y="tip",hue="day")
plt.show()
