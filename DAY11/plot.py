import matplotlib.pyplot as plt
import numpy as np

x=np.array([2022,2023,2024,2025,2026])
y=np.array([38,32,36,33,37])
y1=np.array([50,51,48,50,49])
y2=np.array([40,42,40,41,40])
linestyle=dict(marker=".",
               markersize=20,
               markerfacecolor="black",
               markeredgecolor="yellow",
               markeredgewidth=2,
               linestyle="solid",
               linewidth=3)
plt.xlabel("YEAR", fontsize=20, family="Arial", fontweight="bold", color="blue")
plt.ylabel("STUDENTS", fontsize=20, family="Arial", fontweight="bold", color="blue")
plt.title("CLASS SIZE", fontsize=30, family="sans-serif", fontweight="bold", color="blue")
plt.tick_params(axis="both",colors="blue")
plt.grid(axis="both", linestyle="solid", color="lightblue")
plt.plot(x,y,color="red", **linestyle)
plt.plot(x,y1,color="green", **linestyle)
plt.plot(x,y2,color="blue", **linestyle)
plt.show()
