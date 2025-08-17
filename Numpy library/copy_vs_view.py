import numpy as np
x = np.array([1,2,3,4,5])
y = x.copy()

x[0] = 9
print(x)
print(y)

q = np.array([9,8,7,6,5,4])
e = q.view()
z = q.copy()

print(e.base)
print(z.base)