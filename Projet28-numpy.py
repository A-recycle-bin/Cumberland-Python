# Script de test avec le module numpy, il est utilisé pour travailler avec les arrays
# Numpy représente numerical python, 50x plus rapide que les lists python traditionnelles


import numpy as np

#print(np.__version__)

# 1d array
#arr = np.array([1, 2, 3, 4, 5])

# 2d array
#arr = np.array([[1, 2, 3], [4, 5, 6]])

# 3d array
#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# possible de le definir au depart
#arr = np.array([1, 2, 3, 4], ndmin=5)

#print(arr)
#print(type(arr))

# Retourne la dimension de larray
#print(arr.ndim)

# acceder a des elements de larray
#print(arr[0] + arr[1])

# for a 2d array
#arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#print('2nd element on 1st row: ', arr[0, 1])
#print('Last element from 2nd dim: ', arr[1, -1])

# for a 3d array
#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#print(arr[0, 1, 2])
"""The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6"""

# Dans numpy le type de valeurs est beaucoup plus complexe
# au lieu de 5 types, il y en a 11

#arr = np.array([1, 2, 3, 4])
#arr = np.array(['apple', 'banana', 'cherry'])
#arr = np.array([1, 2, 3, 4], dtype='S')
#print(arr.dtype)

# Changer le type de valeurs en en creant une nouvelle
#arr = np.array([1.1, 2.1, 3.1])
#newarr = arr.astype('i')
#print(arr.dtype)
#print(newarr.dtype)

