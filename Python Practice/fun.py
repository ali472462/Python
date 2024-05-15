import numpy as n
import sys
import time
l= range(1000)
print(f"List:{sys.getsizeof(5)*len(l)}")
array=n.arange(1000)
print(f"Array:{array.size*array.itemsize}")
start=time.time()
a1=n.arange(200000)
a2=n.arange(200000)

add=a1+a2

print((time.time()-start)*1000)

"""////////////////////ADvanced Array in nummpy/////////////////////////////"""

arr=n.array([[2,3,5],[9,7,8]],dtype=complex)
a=arr.ndim

print(arr.itemsize)
print(arr[:, 2])
x=n.zeros((2,3))
print(x)

arr=n.linspace(1,5,15)
print(arr)
ab=n.arange(1,16)
print("a",ab)
ab_reshaped = ab.reshape(3,5)
print(ab_reshaped)

import numpy as np
ab = np.arange(1, 16)
print("a", ab)
ab_reshaped = ab.reshape(3,5)
print(ab_reshaped)
ab_raval=ab.ravel()
print(ab_raval)

print("STD:",n.std(ab))

m=n.array([[1,2],[3,4]])
p=n.array([[5,6],[7,8]])
print(f"{m}\n{p}\n",m.dot(p),m*p)