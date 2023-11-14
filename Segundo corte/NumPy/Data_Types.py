# Se tiene una propiedad llamada dtype que devuelve el tipo de datos de la matriz:
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Creating Arrays With a Defined Data Type
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# Converting Data Type on Existing Arrays
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)


