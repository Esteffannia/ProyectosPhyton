# Cortar en Python significa tomar elementos de un índice determinado a otro índice determinado.

#Corte elementos del índice 1 al índice 5 de la siguiente matriz:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Negative Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

# Step
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

#Silicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

