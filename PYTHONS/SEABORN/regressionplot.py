import seaborn as sns
import matplotlib.pyplot as plt
penguin=sns.load_dataset("penguins")
#regplot - used to represent the regression between two values using linear line
# sns.regplot(data=penguin, x="body_mass_g",y="flipper_length_mm")#shows the regression


# sns.lineplot(data=penguin, x="body_mass_g",y="flipper_length_mm",hue="island",style="sex")#lineplot 

#jointplot - used to represent the data using multiple plots, mostly used to show density 
sns.jointplot(data=penguin, x="body_mass_g", y="flipper_length_mm",hue="island")
plt.show()
