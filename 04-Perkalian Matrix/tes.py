
import numpy as np

print (f"\nPerkalian Matrix\n")

a = np.array ([(1,2), (4,5)])
b = np.array ([(6,7), (8,9)])

print (f"Matrix A :\n{a}\n")
print (f"Matrix B :\n{b}\n")

print ("--------------- Perkalian\n")

hasil = np.dot (a,b)
# bisa juga hasil = a.dot (b)
print (f"Matrix hasil :\n{hasil}\n")

print ("\n")