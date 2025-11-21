import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
squat=np.array([76,96,116,126,136,140,150,160])
bench=([56,66,76,80,85,90,95,100])
deadlift=([76,86,96,106,120,130,140,150])
plt.bar(x,squat)
plt.bar(x,bench)
plt.bar(x,deadlift)
plt.show()