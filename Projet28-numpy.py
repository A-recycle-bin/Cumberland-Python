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

"""
The main difference between a copy and a view of an array is that the copy 
is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array,
 and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made 
to the view will affect the original array, and any changes made 
to the original array will affect the view.
"""

# En copiant, cela ne change pas la valeur dans le array initial
#arr = np.array([1, 2, 3, 4, 5])
#x = arr.copy()
#arr[0] = 42
#print(arr)
#print(x)

# Avec view, la valeur est changée
#arr = np.array([1, 2, 3, 4, 5])
#x = arr.view()
#arr[0] = 42
#print(arr)
#print(x)

# Elle est également changée pour le x qui a été assigné a = l'array
#arr = np.array([1, 2, 3, 4, 5])
#x = arr.view()
#x[0] = 31
#print(arr)
#print(x)

# Pour voir si une variable est `own` ou pas
#arr = np.array([1, 2, 3, 4, 5])
#x = arr.copy()
#y = arr.view()
#print(x.base)
#print(y.base)

# Nous donnera la dimension de l'array (2, 4) se representerait par
# deux colonnes de 4 éléments
#arr = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
#print(arr.shape)

# On peut reshape l'array avec la fonction du meme nom on aura 5 groupes de 2 ici
#newarr = arr.reshape(5,2)
#print(newarr)

# Possible de le reshape en dautres dimensions aussi
#arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#newarr = arr.reshape(2, 3, 2)
#print(newarr)

# Il  y a une fonction pour concatenate des arrays
#arr1 = np.array([1, 2, 3])
#arr2 = np.array([4, 5, 6])
#arr = np.concatenate((arr1, arr2))
#print(arr)

# On peut aussi les splitter
#arr = np.array([1, 2, 3, 4, 5, 6])
#newarr = np.array_split(arr, 3)
#print(newarr)

# Possible dutiliser la fonction where comme une recherche
#The example above will return a tuple: (array([3, 5, 6],)
#Which means that the value 4 is present at index 3, 5, and 6.
#arr = np.array([1, 2, 3, 4, 5, 4, 4])
#x = np.where(arr == 4)
#print(x)

# possible d<ordonner avec numpy egalement
#arr = np.array([3, 2, 0, 1])
#print(np.sort(arr))

# Pour créer des filtres, TRÈS IMPORTANT ICI
#arr = np.array([41, 42, 43, 44])
# Create an empty list
#filter_arr = []
# go through each element in arr
#for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  #if element > 42:
    #filter_arr.append(True)
  #else:
    #filter_arr.append(False)
#newarr = arr[filter_arr]
#print(filter_arr)
#print(newarr)

# Si le nombre est pair
#arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Create an empty list
#filter_arr = []
# go through each element in arr
#for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  #if element % 2 == 0:
    #filter_arr.append(True)
  #else:
    #filter_arr.append(False)
#newarr = arr[filter_arr]
#print(filter_arr)
#print(newarr)