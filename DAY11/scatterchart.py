import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5,6,7,8])
y=np.array([24,30,34,40,43,44,45,49,52])
plt.grid(axis="both")
plt.scatter(x,y,s=150,
            alpha=0.7,
            label="CLASS B"
            )
x1=np.array([0,1,2,3,4,5,6,7,8])
y1=np.array([30,35,40,42,44,48,50,52,56])
plt.scatter(x1,y1,s=150,
            alpha=0.7,
            color="red",
            label="CLASS A")
plt.legend()
plt.show()