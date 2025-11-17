#numpy is a library in python which stands for numerical python and includes array, matrices, etc
import numpy as np
arr = np.array([1,2,3,4,5])#list to create a array
print(arr)
print(type(arr))

#NumPy is used to work with arrays. The array object in NumPy is called ndarray.

#We can create a NumPy ndarray object by using the array() function.

#creating tuple to create a array
arr1=np.array((11,22,33,44,55))
print(arr1)

#DIMENSIONS IN ARRAY
#0D array
arr2=np.array(10)
print(arr2,"\n")

#1D array
arr3=np.array([1,2,3])
print(arr3,"\n")

#2D array
arr4=np.array([[1,2,3],[4,5,6]])
print(arr4,"\n")

#3D array
arr5=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr5,"\n")

#after array name arr.ndim gives the dimension of the array


arr = np.array([1, 2, 3, 4], ndmin=5)
#ndmin allows to assign the number of dimension to the array
print(arr)
print('number of dimensions :', arr.ndim)

#in array indexing starts from 0 
print(arr[0])

#accessing dimesnional array
print(arr5[0, 1])

#slicing an array
arr=np.array([1,2,3,4,5,6])
print(arr[2:4])

arr2=np.array([[1,2,3,4],[6,7,8,9]])
print(arr2[1:3, 2])

#datatypes are also available for numpy
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedeltaw
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

print(arr2.dtype)

arr=np.array(['apple','banana','cherry'])
print(arr.dtype)

'''
Vectorized operations mean performing mathematical operations on entire arrays (vectors, matrices, etc.) without using loops.

Instead of looping through elements manually (like in normal Python lists), NumPy performs these operations internally in optimized C code, making it much faster.
'''
a=np.array([1,2,3,4,5])
b=np.array([1,2,3,4,5])
mul=a*b#vectorized operation
print(mul)


#3 dimensional array
new=np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
              [['a','b','c'],['d','e','f'],['g','h','i']],
              [['a','b','c'],['d','e','f'],['g','h','i']]])
print(new.shape)
print(new[1][2][0])#chain indexing

#slicing
array=np.array([[1,2,3,4],
                [5,6,7,8,],
                [9,10,11,12],
                [13,14,15,16]])
print(array[0:4:2])#array[start:end:step]
print(array[:, 3])#array[:,start:end:step]
print(array[:, ::-1]) 

array=np.array([1,2,3])
print(array + 1)

print(np.sqrt(array))

new_one=np.array([1,1.39,2.23])
print(np.round(new_one))
#np.ceil() and np.floor()

scores=np.array([68,79,55,84,72,32,27,65])
print(scores>50)
print(scores>80)
scores[scores<40]=0
print(scores)

array1=np.array([[1,2,3,4,5,6,7,8,9,10]])
array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array1*array2)

'''
np.sum()-sums the array
np.mean()-returns the mean of the array
np.std()-returns the strandard deviation
np.var()-returns the variance
np.min()-returns the minimum in the array
np.max()-returns the maximum in the array
np.argmin()-returns the position of the min argument
np.argmax()-returns the position of the max argument 
'''