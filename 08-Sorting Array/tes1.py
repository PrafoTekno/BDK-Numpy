
import numpy as np

print ("\nSorting Matrix\n")

a = np.floor (np.random.randn (3,3) * 10)
print (f"Matrix a : \n{a}\n")

print (f"Nilai max a : {a.max ()}")
print (f"Posisi dari {a.max ()} : {a.argmax ()}\n")
print (f"Nilai min a : {a.min ()}")
print (f"Posisi dari {a.min ()} : {a.argmin ()}\n")

print (f"Mengurutkan nilai a : \n{np.sort (a)}\n")
print (f"Mengurutkan nilai a by posisi : \n{np.argsort (a)}\n")

print ("\n")