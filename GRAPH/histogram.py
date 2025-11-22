#histogram is the representation of the distribution of data
import matplotlib.pyplot as plt
import numpy as np

scores=np.random.normal(loc=75,scale=10,size=100)
scores=np.clip(scores,0,100)
plt.title("STUDENT'S SCORE")
plt.xlabel("scores")
plt.ylabel("no. of students")
plt.hist(scores, color="yellow",
        edgecolor="black")
plt.show()
