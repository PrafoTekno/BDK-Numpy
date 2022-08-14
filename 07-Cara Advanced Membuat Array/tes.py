
import numpy as np

print ("\nMembuat Array dengan Cara Advanced\n")

# array dengan tipe data tertentu

a = np.array (([1,2,3], [4,5,6]),dtype = float) 
print (a)

print ("\n")

# array dengan fungsi

def perkalian_5 (baris, kolom):
    return (kolom + baris) * 5

b = np.fromfunction (perkalian_5, (2,3), dtype = int)
print (b)

print ("\n")

# array dengan iterasi 

data = (s for s in range (5))
c = np.fromiter (data , dtype = float)
print (c)

print ("\n")

# Multitype array

tipe = [('nama', 'S255'),('berat', int)]
data = [
    ('Udin', 45),
    ('Sarip', 50),
    ('Joni', 40)
]

d = np.array (data, dtype = tipe)
print (d)

print ("\n")