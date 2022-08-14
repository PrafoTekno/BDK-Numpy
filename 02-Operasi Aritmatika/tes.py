
import numpy as np

print ("\nOperasi Aritmatika\n")

a = [1,2,3,4,5]
b = [1,2,3,4,5]

print (f"List Python : {a + b}")

a = np.array ([1,2,3,4,5])
b = np.array ([1,2,3,4,5])

print (f"\nArray Numpy : {a + b}")
print (f"Array Numpy : {a - b}")
print (f"Array Numpy : {a * b}")
print (f"Array Numpy : {a / b}")

a = np.array ([(1,2,3),(4,5,6)])
b = np.array ([(7,8,9),(1,2,3)])

print (f"\nMatrix numpy :\n{a + b}")
print (f"\nMatrix numpy :\n{a - b}")

print ("\n")