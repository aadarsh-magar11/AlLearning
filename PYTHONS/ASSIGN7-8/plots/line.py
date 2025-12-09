import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
squat=np.array([76,96,116,126,136,140,150,160])
bench=([56,66,76,80,85,90,95,100])
deadlift=([76,86,96,106,120,130,140,150])
line=dict(marker="*",
               markersize=10,
               mec="yellow",
               mfc="red",
               linestyle="solid"
               )
plt.grid(axis="both",color="lightblue")
plt.title("WEIGHT PROGRESS",fontsize=20)
plt.plot(x,squat,**line,color="red",label="squat")
plt.plot(x,bench,**line,color="green",label="bench")
plt.plot(x,deadlift,**line,color="blue",label="deadlift")
plt.xlabel("red-squat,green-bench,blue-deadlift")
plt.ylabel("WEIGHT")
plt.legend()
plt.show()