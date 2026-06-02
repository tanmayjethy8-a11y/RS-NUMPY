#Difference between dtype & astype:
import numpy as np
a=np.array([1,2,3,4])
print("dtype:",a.dtype)#shows datatype of array
print("astyp:",a.astype(complex)) #converts datatype of array from one to another
print("original array",a)