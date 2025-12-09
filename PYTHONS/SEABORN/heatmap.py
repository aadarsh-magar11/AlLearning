import matplotlib.pyplot as plt
import seaborn as sns
data=sns.load_dataset("penguins")
columns=["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]
sns.heatmap(data=data[columns].corr(), annot=True, linewidth=2, vmin=-0.2, cmap="Reds", linecolor="black")
plt.show()