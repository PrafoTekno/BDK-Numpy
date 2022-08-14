
import numpy as np

print ("\nInvers dan Determinan\n")

a = np.array (([0,1], [-1,0]))
print (f"Matrix a :\n{a}\n")

a_inv = np.linalg.inv (a)
print (f"Invers a :\n{a_inv}\n")

print (4*"-" + " Cek " + 4*"-" + "\n")

hasil = np.dot (a, a_inv)
print (f"Hasil a * a': \n{hasil}\n")

det_a = np.linalg.det (a)
print (f"Determinan a : {det_a}")
det_a_inv = np.linalg.det (a_inv)
print (f"Determinan a' : {det_a_inv}")

print ("\n")

