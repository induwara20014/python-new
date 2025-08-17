import numpy as np

arr = np.array([1,2,3,4,5,6,7])

x = np.where(arr == 4)
z = np.where(arr%2==0)
print(x)
print(z)

arr1 = np.array([[1,2],[3,4]])
y = np.where(arr1 == 3)
print(y)

print("------------------------------------------------")

arr2 = np.array([1,3,5,9])
x = np.searchsorted(arr2,4)
y = np.searchsorted(arr2,[2,3,8])
print(y)
print(x)
z = np.searchsorted(arr2,4,side='right')
print(z)

