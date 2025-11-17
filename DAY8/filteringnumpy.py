import numpy as np

ages=np.array([[21,17,28,30,14,58,18,42],
               [39,22,15,98,43,56,13,17]])

teenagers=ages[ages<18]
adults=ages[(ages>=18) & (ages<=65)]
seniors=ages[ages>65]
print(teenagers)
print(adults)
print(seniors)
  
#random number generator using numpy
rng=np.random.default_rng()
print(rng.integers(low=1,high=7))
#can also assign the size of the array
print(rng.integers(low=1,high=101,size=(3,2)))

#shuffle an array
array=np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)