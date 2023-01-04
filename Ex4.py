from numpy import array
from scipy.linalg import svd
A = array([[12, 21, 39], [94, 75, 46],[37, 80, 94], [64, 34, 99], [38, 12, 89]])
U, s, VT = svd(A)
print('Decomposed matrix:\n', U) #decomposed matrix
print('Inverse matrix:\n', s) #inverse matrix
print('Transpose matrix:\n', VT) #transpose of matrix