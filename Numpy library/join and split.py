import numpy as np

#concatenate

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9])

newarr = np.concatenate((arr1,arr2))
print(newarr)

arr3 = np.array([[10,20,30],[40,50,60]])
arr4 = np.array([[70,80,90],[20,40,60]])

newarr1 = np.concatenate((arr3,arr4),axis=0)
print(newarr1)

newarr2 = np.concatenate((arr3,arr4),axis=1)
print(newarr2)

#array_split()

arr = np.array([1,2,3,4,5,6])

newarr3 = np.array_split(arr,3)
print(newarr3)
newarr4 = np.array_split(arr,4)
print(newarr4)

arr = np.array([[1,2],[3,4],[5,6],[7,8]])

newarr5 = np.array_split(arr,2)
print(newarr5)


