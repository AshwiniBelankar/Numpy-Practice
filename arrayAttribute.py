import numpy as np
a = np.array([[2,5,6],[7,8,9]])
print(a)
print(a.shape)
a.shape = (3,2)
print(a)
b = np.arange(24)
print(b)
b.ndim

c = b.reshape(2,4,3)
print(c)

x = np.empty([3,2], dtype = int)
print(x)
