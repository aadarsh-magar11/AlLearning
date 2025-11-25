import matplotlib.pyplot as plt
import numpy as np
x1=np.array([1,2,3,4,5,6,7,8,9,10])
y1=np.array([55,43,45,53,49,48,56,37,40,42])
y2=np.array([35,48,55,59,54,44,45,43,36,45])
plt.scatter(x1,y1,s=140,color="red",label="class A")
plt.scatter(x1,y2,s=140,color="green",label="class B")
plt.show()