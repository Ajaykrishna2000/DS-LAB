import numpy as np

#Matrixes as ndarray objects
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[8,9]])
print("a",  type(a))
print(a)
print("b",  type(b))
print(b)

#Matrixes as matrix objects
c = np.array([[1,2],[3,4]])
d = np.array([[5,6],[8,9]])
print("\nc",  type(c))
print(c)
print("\nd",  type(d))
print(d)
print("\n* Operation on two ndarray objects (Elementwise)")
print(a * b)
print("\n* Operation on two matrix objects (same as np.dot())")
print(c * d)