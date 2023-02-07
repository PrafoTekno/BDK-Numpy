
import numpy as np
import math as mt

print ("\nMembuat Array\n")

# Membuat vector 

a = np.array ([1,2,3,4,5])
b = np.array ([1.5,4.6,9,3])

#print (mt.pi)

#print ("\n")

print (a)
print (b)

# Membuat vector dengan range

c = np.arange (1,10,4)
print (c)

# Membuat vector dengan linspace

d = np.linspace (1,10,3)
print (d)

# Membuat matrix 

e = np.array ([(1,2,3), (4,5,6)])
print (e)

# Membuat matrix dengan nilai 0

f = np.zeros ((4,4))
print (f)

# Membuat matrix dengan nilai 1

g = np.ones ((4,4))
print (g)

# Membuat matrix indentitas

h = np.identity (6)
print (h)
h1 = np.eye (6)
print (h1)

print ("\n")
