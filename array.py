import numpy as  np

print(np.__version__)

x = np.array([1,2,3,4,5],ndmin=4)
print(x)
print(x.ndim)

# can i have using list and tuple

y = np.array([2,4,6,8])
print(y)

z = np.array((2,3,4,5,6,7,8))
print(z)

#2D array

s = np.array([[1,2,3,4],[6,7,8,9]])
print(s)

#3D array

q = np.array([[[1,2],[6,7]],[[9,5],[4,2]]])
print(q)
print(q.ndim)
 