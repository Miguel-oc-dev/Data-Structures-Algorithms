"""
#Given two sorted arrays, we need to merge them and create one big sorted array.
#For example, array1 = [1,3,5,7], array2 = [2,4,6,8]
#The result should be array = [1,2,3,4,5,6,7,8]
"""

def merge(array1, array2):
    new_array = []
    # Dos punteros para los respectivos arreglos
    i = j = 0

    # Compara los elementos de ambos arrays
    while i < len(array1) and i < len(array2):
        if array1[i] <= array2[j]:
            new_array.append(array1[i])
            i += 1
        else:
            new_array.append(array2[j])
            j += 1

    # Agrega elementos restantes de cualquiera de los dos arrays
    new_array.extend(array1[i:])
    new_array.extend(array2[j:])

    return new_array 

array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8, 10]

print(merge(array1, array2))