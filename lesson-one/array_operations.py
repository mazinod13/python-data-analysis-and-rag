import numpy as np
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)
c= a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a>35)


#products in array
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])

print(A*B) #elementwise product
print(A@B) #matrix product
print(A.dot(B)) #another way of matrix product

#modifying the shape of an array
rg = np.random.default_rng(1)
a = np.ones((2, 3), dtype=np.int_)
b = rg.random((2, 3))
a *= 3
print(a)
b += a
print(b)

#array with different types
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, np.pi, 3)
print(b.dtype.name)
c = a + b
print(c)

d = np.exp(c * 1j)
print(d)
print(d.dtype.name)

#unary operations
a = rg.random((2, 3))
print(a)
print(a.sum())
print(a.min())
print(a.max())

#axis operations
b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum(axis=0)) #sum of each column
print(b.min(axis=1)) #min of each row
print(b.cumsum(axis=1)) #cumulative sum along each row

