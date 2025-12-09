import matplotlib.pyplot as plt
import numpy as np

exercise=np.array(["bench","deadlift","squat","curls","extension"])
intensity=np.array([3,4,5,3,5])

plt.bar(exercise,intensity,color="green")
plt.xlabel("exercise", color="blue", fontsize=20, fontfamily="Arial")
plt.ylabel("intensity", color="blue", fontsize=20, fontfamily="Arial")
plt.show()
