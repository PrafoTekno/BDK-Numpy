
import numpy as np

print ("\nSorting Array Mulitype\n")

tipe = [('nama','S255'), ('tinggi', int), ('berat', int)]

data = [

    ('Naruto', 176, 55),
    ('Saitama', 174, 58),
    ('Gon', 150, 42)

]

a = np.array (data, dtype = tipe)
print (f"Array data : \n{a}\n")

print (f"Sort by nama : \n{np.sort (a, order = 'nama')}\n")
print (f"Sort by tinggi : \n{np.sort (a, order = 'tinggi')}\n")
print (f"Sort by berat : \n{np.sort (a, order = 'berat')}\n")

print ("\n")