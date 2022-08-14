
import numpy as np

print ("\nSorting Array\n")

a = np.floor (np.random.randn (1,6) * 10)
print (f"Array a : {a}\n")

print (f"Nilai max a : {a.max ()}")
print (f"Posisi dari {a.max ()} : {a.argmax ()}\n")
print (f"Nilai min a : {a.min ()}")
print (f"Posisi dari {a.min ()} : {a.argmin ()}\n")

print (f"Mengurutkan nilai a : {np.sort (a)}")
print (f"Mengurutkan nilai a by posisi : {np.argsort (a)}\n")

print ("\n")