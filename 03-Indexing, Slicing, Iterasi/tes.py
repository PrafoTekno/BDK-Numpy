
import numpy as np

print ("\nIndexing, Slicing, Iterasi\n")

data = np.arange (1,10) * 2
print (f"Data array : {data}\n")

# Indexing 

print (f"Element ke 2 dari data : {data[2]}")
print (f"Element terakhir dari data : {data[-1]}")

# Slicing

print (f"Elemnt dari 1-4 dari dat : {data[1:5]}")
print (f"Element dari 3-akhir dari data : {data[3:]}")
print (f"Element dari awal-6 dari data : {data[:6]}\n")

# Iterasi 

for s in data :
    print (f"Nilai : {s}")

print ("\n")