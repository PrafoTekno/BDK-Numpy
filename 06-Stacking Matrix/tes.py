
import numpy as np

print ("\nStacking Matrix\n")

a = np.array (([1,2,3],[4,5,6]))
b = np.array (([-1,-2,-3],[-4,-5,-6]))
c = np.array ((10,9,11))

print (f"Matrix a : \n{a}\n")
print (f"Matrix b : \n{b}\n")

print (f"Matrix hstack : \n{np.hstack ((a,b))}\n")
print (f"Matrix vstack : \n{np.vstack ((a,b))}\n")
print (f"Matrix vstack : \n{np.vstack ((a,c))}\n")

# Perhatikan jumlah kolom dan baris

print ("\n")
