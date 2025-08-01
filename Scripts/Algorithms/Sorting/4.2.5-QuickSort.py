"""
Quick Sort
Is another sorting algorithm which follows divide and conquer.
It requires to choose a pivot, then place all elements smaller than the pivot on the left and all larger on the right
then the array is parttioned in the pivot position.

Complexity: O(n log n)
"""

count = 0

# Esta funcion sirve para partir el arreglo
def partition(array, left, right):
    # Indice del ultimo elemento mas peque;o
    smallerIndex = left - 1
    # Ultimo elemento como pivote
    pivot = array[right]
    
    for i in range(left, right):
        global count
        count += 1
        # Si el elemento es menor que el pivote
        if array[i] < pivot:
            # Aumentamos el indice del menor y hacemos cambio
            smallerIndex += 1
            array[smallerIndex], array[i] = array[i], array[smallerIndex]
    
    # Colocamos el pivote en su posicion ordenada
    array[smallerIndex+1], array[right] = array[right], array[smallerIndex+1]
    print(array)
    return(smallerIndex+1)


# Funcion de ordenamiento
def quickSort(array, left, right):
    if left < right:
        # Obtenemos la posicion del pivote
        partitioningIndex = partition(array, left, right)
        print(partitioningIndex)
        # Llamadas recursivas para izquierda y derecha
        quickSort(array, left, partitioningIndex - 1)
        quickSort(array, partitioningIndex + 1, right)

array = [5,9,3,10,45,2,0]
quickSort(array, 0, (len(array)-1))
print(array)
print(f'Number of comparisons = {count}')

