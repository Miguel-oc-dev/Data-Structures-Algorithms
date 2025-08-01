"""
Merge Sort
Use divide and conquer. It involves breaking up the array from the middle
arrays of only 1 element remain thein merging them up in a sorter order

Complexity: O(nlog N)
"""

count = 0

def mergeSort(array):
    # Caso base: si el arreglo tiene 1 o 0 elementos, ya esta ordenado
    if len(array) <= 1:
        return array
    else:
        # Dividimos el arreglo en dos mitades
        mid = len(array) // 2
        izquierda = mergeSort(array[:mid])
        derecha = mergeSort(array[mid:])

        print(f'Izquierdo : {izquierda}')
        print(f'Derecho : {derecha}')

        # Combinamos las dos mitades ordenadas
        return merge(mergeSort(izquierda), mergeSort(derecha))

def merge(izquierda, derecha):
    i = len(izquierda)
    d = len(derecha)

    indexIzquierdo = 0
    indexDerecho = 0

    arrayOrdenado = []

    while(indexIzquierdo < i and indexDerecho < d):
        global count
        count += 1
        if izquierda[indexIzquierdo] < derecha[indexDerecho]:
            arrayOrdenado.append(izquierda[indexIzquierdo])
            indexIzquierdo += 1
        else:
            arrayOrdenado.append(derecha[indexDerecho])
            indexDerecho += 1
    
    print(arrayOrdenado + izquierda[indexIzquierdo:] + derecha[indexDerecho:])
    return arrayOrdenado + izquierda[indexIzquierdo:] + derecha[indexDerecho:]

array = [5,9,3,10,45,2,0]
sorted_array = [5,6,7,8,9]
reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]

print(mergeSort(array))
print(f'Number of comparisons = {count}')
