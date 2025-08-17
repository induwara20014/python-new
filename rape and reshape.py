import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
print(arr.shape)

print("-----------------------------------------------")

arr1 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr1)
print(arr1.shape)

#ndmin keyword

arr2 = np.array([9,7,5,3,1],ndmin=5)
print(arr2)
print(arr2.shape)

print("-------------------------------------------")
arr3 = np.array([1,2,3,4,5,6,7,8,9])
new1 = arr3.reshape(3,3)
print(new1)
new2 = arr3.reshape(9,1)
print(new2)
new3 = arr3.reshape(1,9)
print(new3)


arr4 = np.array([1,2,3,4,5,6,7,8])
new4 = arr4.reshape(2,2,2)
print(new4)

arr5 = np.array([11,12,13,14,15,16,17,18])
new5 = arr5.reshape(2,2,-1)
print(new5)

arr6 = np.array([[1,2,3],[4,5,6]])
new6 = arr6.reshape(-1)
print(new6)