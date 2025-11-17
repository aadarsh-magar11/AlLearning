import matplotlib.pyplot as plt
import numpy as np
#drawing a line 
xpoints = np.array([0,6])#these are x-cordinates
ypoints = np.array([0,200])#these are y-cordinates

plt.plot(xpoints,ypoints)
plt.show()

# plt.plot(xpoints,ypoints,'o')#'o' is a prameter that is used to show the points rather then forming a line
# plt.show()

#froming mulitple points
x = np.array([0,5,25,125])
y = np.array([12,144,60,96])
plt.plot(x,y)
plt.show()

#we can plot the graph without specifying the x co-ordinates as it will take default points 0,1,2,3,4,...
mountain=np.array([5,15,5,15,5,15,5])
plt.plot(mountain)
plt.show()

#marker are used to highlight the points, marker='o'or'*'or other marker 
plt.plot(mountain,marker='*',ms=20, mec='m', mfc='r')#ms is marker size, mec means marker color, mfc means marker face color
plt.show()

#graph can be designed too using 'fmt' parameter in the sequence marker|line|color
plt.plot(mountain,'*--g')
plt.show()