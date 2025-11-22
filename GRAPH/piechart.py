import matplotlib.pyplot as plt
import numpy as np

expense=["EDUCATION","RENT","FOOD","CLOTH","HEALTH","MISCELLEOUS"]
values=np.array([25000,15000,12000,10000,5000,10000])
colors=["red","green","blue","cyan","magenta","teal"]
plt.title("MONTHLY EXPENDITURE",
          fontsize=20,
          fontfamily="arial")
plt.pie(values, labels=expense,
        colors=colors,
        autopct="%1.1f%%",
        explode=[0.1,0,0,0,0,0],
        shadow=True,
        startangle=270
        )
plt.show()