def binarySearch(array, target):
    # Definimos los extremos del arreglo
    left = 0
    right = len(array) - 1

    # Continuemos mientras los extremos no se crucen
    while left <= right:
        # Indice del medio
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            # Buscando en la mitad derecha
            left = mid + 1
        else:
            # Buscando en la mitad izquierda
            right = mid - 1

    return - 1

arr = [1, 3, 5, 7, 9, 11]
target = 7
print('Buscando: ', target)
print("Índice del objetivo:", binarySearch(arr, target))
