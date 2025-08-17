import numpy as np

#1D array

arr = np.array([2,4,6,8])
print(arr)
print(arr[2])
print(arr[2]+arr[0])

#2D array

arr2 = np.array([[1,2,3],[5,6,7],[8,9,10]])
print(arr2)
print(arr2[1,0])

#3D array

arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr3)
print(arr3[1,1,1])

#negetive indexing

arr4 = np.array([3,4,5,6,7,8])
print(arr4[-4])