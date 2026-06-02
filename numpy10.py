import numpy as np
a=np.array([[2,4,6],[8,10,12]])
print("ARRAY:",a)
print("shape:",a.shape)
print("size:",a.size)
print("ndim:",a.ndim)
print("dtype:",a.dtype)
b=a.astype(complex)
print("Array with complex data type:",b)
