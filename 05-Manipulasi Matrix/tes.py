
import numpy as np

print ("\nManipulasi Matrix\n")

A = np.array (([1,2,3], [4,5,6]))

print (f"Matrix A :\n{A}")
print (f"Ukuran matrix A : {A.shape}\n")

# A.transpose ()
# np.transpose (A)
# A.T

print (f"Transpose Matrix A :\n{A.transpose ()}")
print (f"Ukuran matrix A : {A.shape}\n")

# vector baris, flatten

print (f"Vector baris Matrix A :\n{A.flatten ()}")
print (f"Ukuran matrix A : {A.shape}\n")

# reshape matrix

print (f"Matrix A :\n{A.reshape (6,1)}")
print (f"Ukuran matrix A : {A.shape}\n")

# resize matrix

print (f"Matrix A :\n{A.resize (3,2)}")
print (f"Ukuran matrix A : {A.shape}\n")


print ("\n")