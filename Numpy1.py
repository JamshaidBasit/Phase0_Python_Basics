#5. NumPy (The Backbone of ML)
#Python ki lists slow hoti hain, NumPy arrays fast aur memory efficient hote hain.
#Key Concepts:
#Creation: np.array(), np.zeros(), np.ones(), np.arange().
#Shape & Reshape: Array ki dimension check karna aur badalna.
#Broadcasting: Chote array ko bade array ke saath math perform karne ke liye "khichna".
#Matrix Operations: Dot product (np.dot) aur Matrix multiplication (@).

import numpy as np
a1=np.array([1,2,3])  ## 1 Dimension
print(a1)
print(a1.ndim)
#################################################################################################
a2=np.array([[1,2,3],[4,5,6]])
print(a2)
print(a2.ndim)
##################################################################################################
a3=np.zeros(3)  ## 1D zeros
print(a3)

a31=np.zeros((3,4))
print(a31)
##################################################################################################
a4=np.ones(4)
print(a4)
##################################################################################################
a41=np.arange(4)
print(a41)
#################################################################################################
# Dot Product (Neural Networks ka base)
v1 = np.array([1, 2])
v2 = np.array([3, 4])
dot_prod = np.dot(v1, v2) # (1*3 + 2*4) = 11
print(dot_prod)
################################################################################################
##Matrix Multiplication
mat_prod=v1@v2
print(mat_prod)
#############################################################################################
# 4. Determinant & Inverse (Used in solving linear equations)
#det = np.linalg.det(v1)
#inv = np.linalg.inv(v2)
