
import numpy as np
import matplotlib.pyplot as plt

print ("\nMenampilkan Plot Data\n")

x = np.arange (1,11)
y = x * 2 + 7

print (f"Vector x : {x}")
print (f"Vector y : {y}")

# Menampilkan plot/grafik

# plt.plot (x,y)
# plt.show ()

# Membuat lingkaran

r = 6
sudut = np.linspace (0,2*np.pi,200)

x = r * np.cos (sudut)
y = r * np.sin (sudut)

plt.plot (x,y)
plt.show ()

print ("\n")