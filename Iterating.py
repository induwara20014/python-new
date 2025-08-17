import numpy as np

arr = np.array([1,2,3,4,5])
for i in arr:
    print(i)

print("--------------------------------------------------")

arr1 = np.array([[1,2,3],[4,5,6]])
for i in arr1:
    for j in i:
        print(j)

print("--------------------------------------------------")

arr2 = np.array([[9,8,7],[6,5,4]])
for i in np.nditer(arr2[:,::2]):
    print(i)

print("--------------------------------------------------")

arr3 = np.array([[6,7,8],[4,3,2]])
for i,j in np.ndenumerate(arr3):
    print(i,j)