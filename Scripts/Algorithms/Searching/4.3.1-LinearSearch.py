def linearSearch(array, target):

    # Recorremos la lista elemento por elemento
    for i in range(len(array)):
        
        # Verificamos si el elemento actual es igual al target
        if array[i] == target:
            return i
    return -1

nums = [4, 2, 7, 1, 9, 3]
target = 1
resultado = linearSearch(nums, target)
print(f"Índice del elemento {target}:", resultado)


""" 
Ejercicio
Escribe una funcion que devuelva todos los indices donde se encuentra el valor buscado
"""

def indexSearch(array, target):
    indices = []
    for i in range(len(array)):
        if array[i] == target:
            indices.append(i)
    return indices

print(indexSearch([5, 2, 5, 1, 5], 5))  # [0, 2, 4]

