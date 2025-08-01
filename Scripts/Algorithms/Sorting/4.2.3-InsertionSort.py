"""
Insertion Sort

For the first iteration we fix the first element, assuming it is at correct position
Then, we loop through the rest of elements and insert them in their correct positions, with respect to the already sorted part

Complexity: O(n^2)
"""

def insertionSort(array):
    count = 0

    # Recorremos cada posicion del arreglo desde la posicion 1
    for i in range(1, len(array)):
        print(array)

        # Se guarda el valor actual que vamos a insertar en su lugar correcto
        current = array[i]
        # Comparamos el elemento anterior con el actual
        j = i - 1
        # Se aumenta el contador
        count += 1

        # Desplazamos a la derecha todos los elementos mayores que "current"
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            # Retrocedemos para comparar con el elemento anterior
            j -= 1
            count += 1

        # Insertamos current en su posicion correcta, dentro de la parte ordenada
        array[j + 1] = current
    
    return (f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(insertionSort(array))


"""
Example
Segunda manera en la que se puede realizar insertion sort 
"""
def insert(array):
    for i in range(len(array)):
        if array[i] < array[0]:
            # Mueve el numero al principio
            num = array.pop(i)
            array.insert(0, num)
        else:
            # Encontrar dónde debería ir el número
            for j in range(1, i):
                if array[i] > array[j - 1] and array[i] < array[j]:
                    num = array.pop(i)
                    array.insert(j, num)
                    break
    return array

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(insert(numbers))


"""
Ejercicio 1
Crea una funcion llamada ordenarEdades que reciba una list de edades de personas
y las ordene.
"""

def ordenarEdades(edades):
    for i in range(1, len(edades)):
        current = edades[i]
        j = i - 1

        while j >= 0 and edades[j] > current:
            edades[j + 1] = edades[j]
            j -= 1
        edades[j + 1] = current
    return(f'\nEdades ordenadas: {edades}')

edades = [29, 15, 42, 18, 23, 36]
print(ordenarEdades(edades))