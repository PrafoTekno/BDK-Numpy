
import numpy as np 

print ("\nPerkalian Dot & Cross\n")

a = np.array ([1,2,3])
b = np.array ([4,3,5])

print (f"Vector a : {a}")
print (f"Vector b : {b}\n")

hasil = np.dot (a,b)
print (f"a dot b = {hasil}\n")

hasil = np.cross (a,b)
print (f"a cross b = {hasil}")

hasil = np.cross (b,a)
print (f"b cross a = {hasil}")

print ("\n")