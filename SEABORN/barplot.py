import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data=sns.load_dataset("penguins")
# sns.barplot(data=data, x="species", y="body_mass_g",hue="sex",
#              palette=["blue","pink"],
#              estimator=np.sum)
sns.countplot(data=data, x="species", hue="island", palette=["red","green","blue"])
plt.title("species and bodymass relation")
plt.show()