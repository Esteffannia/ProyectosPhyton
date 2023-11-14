# El objeto de matriz en NumPy se llama ndarray.
# Se crea un ndarray objeto NumPy usando la array()función.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Matriz 0-D
arr = np.array(42)
print(arr)

# Matriz 1-D
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Matriz 2-D
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Matriz 3-D
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

# Verfificar número de dimensiones (ndim)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Dimesnsiones superiores utilizando ndim argumento
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)


