
import numpy as n
import sys
import time
"""
l= range(1000)
print(f"List:{sys.getsizeof(5)*len(l)}")
array=n.arange(1000)
print(f"Array:{array.size*array.itemsize}")
start=time.time()
a1=n.arange(200000)
a2=n.arange(200000)

add=a1+a2

print((time.time()-start)*1000)


//////////////////ADvanced Array in nummpy///////////////////////////// 

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


                    #"indexing and Slicing in Arrays """
"""
Arr=n.array([1,2,3,4,5,6,7,8,9])
#its slicing 
print(f"Slicing {Arr[0:2]}{Arr[-1]}")
Arr_resp=Arr.reshape([3,3])
print(f"RE-Shaping :{Arr_resp}\n")
print(f"Slicing: {Arr_resp[0:3,1]}Last Element :{Arr_resp[2,1:3]}Hello{Arr_resp[1:3,:]}")

# Iterating Through the arrays 
for value in Arr_resp.flat:
    print(value)
Arr_k=n.zeros([3,3])
for row in range(3):
    for col in range(3):
        Arr_k[row,col]=int(input(f"Enter value at Index[{row}],[{col}] : {Arr_k[row,col]}"))
for value in Arr_k.flat:
    print(value)          #Print Two  Dimensional array In Short Way

print(Arr_k) 
"""
#//////////////////////              Array stacking               ///////////////////////////////
dx=n.arange(6).reshape(2,3)
print(dx)
dy=n.arange(6,12).reshape(2,3)
print(dy)

# NOw Let Stacking Array

print(n.vstack((dx,dy))) #just Printing
#can also store into another var

dd=n.hstack((dx,dy))
print(f"Like This: {dd}")

#H_split  and Vsplit
p=n.arange(2,32).reshape(2,15)
print(p)
p_s= n.hsplit(p,3)
print(f"\n\n1: {p_s[0]}\n\n2: {p_s[1]}\n\n3: {p_s[2]}\n\n")

p=n.arange(2,32).reshape(2,15)
print(p)
p_s= n.vsplit(p,2)
print(f"\n\n1: {p_s[0]}\n\n2: {p_s[1]}\n\n")


#              ////////////////////////// INDEXING With Boolean Arrays////////////////////////

m=n.arange(20).reshape(4,5)
b=m<3
m[b]=5
print(f"{m}\n\n{b}\n\n{m[b]}")

a=n.arange(2,14).reshape(3 ,4)
print(a)
#for row in a:
#    for cell in row:
#        print(f"hello: {cell}")
#for x in n.nditer(a,order='C'):
 #   print(x)

for x in n.nditer(a,order='F',flags=['external_loop']):
    print(f"Fortran: {x}")
# Example 6: Using the buffered flag
arr = n.array([1, 2, 3])
it = n.nditer(arr, flags=['buffered'])
for x in it:
    print(x)
# Example 6: Using the multi_index flag
arr = n.array([[1, 2], [3, 4]])
it = n.nditer(arr, flags=['multi_index'])
for x in it:
    print(x, it.multi_index)
# Example 6: Using the zerosize_ok flag
arr = n.array([])
it = n.nditer(arr, flags=['zerosize_ok'])
for x in it:
    print('This should not be printed')

for x in n.nditer(a,op_flags=['readwrite']):
    x[...] = x * x
    print(f"Square: {a}")
import numpy as np

b = np.arange(4, 16, 4).reshape(3, 1)
print(b)

for x,y in n.nditer([a,b]):
    print(x,y)