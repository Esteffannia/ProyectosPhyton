# La principal diferencia entre una copia y una vista de una matriz es que la copia es una nueva matriz y la vista es solo una vista de la matriz original.

# Copy:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

#View
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

# Check if Array Owns its Data
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)