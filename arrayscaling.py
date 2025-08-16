import numpy as np

#1D array
arr = np.array([1,2,3,4,5])
print(arr)
#arr[start:end]
print( arr[:] )
print(arr[:4])
print(arr[2:])
print(arr[1:4])
print(arr[-4:-1])

# comment

#arr[start:end:step]
print(arr[1::2])
print(arr[::2])

#2D array
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])




