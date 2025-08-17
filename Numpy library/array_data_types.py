import numpy as np

x = np.array([1,2,3,4])
print(x)
print(x.dtype)

y = np.array(['python','java','c++'])
print(y.dtype)

#dtype function

z = np.array([5,6,7,8,9],dtype='f')
print(z)
print(z.dtype)

#astype function

q = np.array([9,8,7,6,5,4])
print(q)
print(q.dtype)
r = q.astype('f')
print(r)
print(r.dtype)

e  = np.array([1.2,9.7,0,6.5,4.3,0,7.9,4.1])
u = e.astype(bool)
print(u)
print(u.dtype)
