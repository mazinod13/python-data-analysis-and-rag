import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.data)
print(type(a))

b = np.array([6,7,8])
print(b)
print(type(b))