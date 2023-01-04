import numpy as np

#Matrixes as ndarray objects
a = np.array([[2,3,5],[3,3,4]])
b = np.array([[1,5,6],[2,8,9]])
c = np.array([[4,1,3],[7,5,8]])
print("a",  type(a))
print(a)
print("b",  type(b))
print(b)
print("c",  type(c))
print(c)

print("\nMultiplication of (a*b)*c is:")
print((a * b) * c)
print("\nMultiplication of a*(b*c) is:")
print(a * ( b * c))