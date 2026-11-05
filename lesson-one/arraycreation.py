#array from a regular python list or tuple using the array() function
import numpy as np
a = np.array([2, 3, 4])
print(a)
print(a.dtype) #int64

b = np.array([1.2, 3.5, 5.1])
print(b)
print(b.dtype) #float64

#array transforms sequences of sequences into 2-D arrays and similarly 3-D and so on
b = np.array([(1.5,2,3), (4,5,6)])
print(b)
print(b.dtype)

#type of array explicitly specified
c = np.array([[1,2],[3,4]], dtype=np.complex128)
print(c)#[[1.+0.j 2.+0.j]
        # [3.+0.j 4.+0.j]]
print(c.dtype) #complex128

#full zero array
print(np.zeros((3,4))) #3 rows and 4 columns


#full one array
print(np.ones((2,3,4),dtype=np.int16)) #2 blocks of 3 rows and 4 columns

#empty array content are random and depend on the state of the memory. The array is allocated but not initialized
print(np.empty((2,3))) #2 rows and 3 columns

#arange function to create sequences of numbers
print(np.arange(10,30,5)) #start at 10, stop before 30, step by 5

print(np.arange(0,2,0.3)) #start at 0, stop before 2, step by 0.3

#linspace function to create sequences of numbers
from numpy import pi
print(np.linspace(0,2,9)) #start at 0, stop at 2, 9 numbers in total

x = np.linspace(0,2*pi,100) #start at 0, stop at 2*pi, 100 numbers in total
f = np.sin(x)
print(f)