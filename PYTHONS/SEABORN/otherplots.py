import matplotlib.pyplot as plt
import seaborn as sns
# rugplot used to show the relation on the basis of the data given
penguin=sns.load_dataset("penguins")
# sns.rugplot(data=penguin, x="body_mass_g", hue="species", palette="Set2",height=1.5, linewidth=2)


#pairplot= gives the plot of all the numerical data of the dataset
# sns.pairplot(data=penguin, diag_kind="kde",hue="island")


#pair grid = pair grid can be used to show the relation through different graphs it has 3 parts upper_triangle, diagonal, lower_trinagle
graph=sns.PairGrid(data=penguin, hue="sex")
graph.map_upper(sns.scatterplot)
graph.map_diag(sns.kdeplot)
graph.map_lower(sns.lineplot)


plt.show()


