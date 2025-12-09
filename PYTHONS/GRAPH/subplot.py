#subplot is used to make multiple plots in the single canvas
#made using figure and subplot()
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])

figure, axes=plt.subplots(2,2)
axes[0,0].plot(x, x**2, color="red")
axes[0,0].set_title("linegraph")

axes[0,1].bar(x,x*2-1)
axes[0,1].set_title("bargraph")

nums=np.random.normal(loc=50,scale=5,size=25)
axes[1,0].hist(nums)
axes[1,0].set_title("histograph")

axes[1,1].pie(x, autopct="%1.1f%%")
axes[1,1].set_title("piechart")
plt.show()