#2. Linear Algebra (NumPy implementation)
#Linear Algebra data ko store aur process karne ka tarika hai.
#Vectors
##magnitude
##addition
##dot product
#Matrices
##multiplication
##transpose
##inverse
###determinant
#Eigenvalues & Eigenvectors
##kya hote hain

#####################################################################################################
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[10,20],[5,10]])
##Addition
print(np.add(arr1,arr2))
###Dot Product
print(np.dot(arr1,arr2))
## Multiplication
print(arr1@arr2)
##Transpose
print(arr1.T)
## Determinent
print(np.linalg.det(arr1))
## Inverse
print(np.linalg.inv(arr1))

#Eigenvalues & Eigenvectors (PCA ka base)
values, vectors = np.linalg.eig(arr1)
print(f"Eigenvalues: {values}")
print(f"Eigen Vectors:{vectors}")

####################################################################################################
