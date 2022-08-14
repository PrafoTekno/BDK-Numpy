
import numpy as np

print ("\nSolusi Persamaan Linear\n")

A = np.array (([2,3], [1,2]))
Y = np.array ([23,14])

print (A, "\n")

A_inverse = np.linalg.inv (A)

# Hasil

hasil_1 = np.dot (A_inverse, Y)
print (hasil_1)

hasil_2 = np.linalg.solve (A, Y)
print (hasil_2)

print ("\n")