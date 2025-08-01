"""
Selection Sort
Involves finding the minimun element in one pass through the array
and then swapping it with the first position of the unsorted of the array

Complexity: O(n^2)
"""

def selectionSort(array):
    count = 0

    # Recorremos cada posicion del arreglo excepto la ultima linea
    for i in range(len(array) -1):
        print (array)
        minimum = array[i]
        minimum_index = i

        # Buscamos el elemento mas pequeño en el resto del arreglo
        for j in range(i + 1, len(array)):
            count += 1
            if array[j] < minimum:
                #Si encontramos un elemento más pequeño, actualizamos el minimo
                minimum = array[j]
                minimum_index = j

        # Al terminar el ciclo interno, se encuentra un nuevo minimo, lo intercambiamos        
        if minimum_index != i:
            # Intercambiamos el valor minimo encontrado con el valor actual
            array[minimum_index], array[i] = array[i], array[minimum_index]
    return(f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(selectionSort(array))


reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
print(selectionSort(reverse_sorted_array))


"""
Ejercicio 1
Escribe una fucion "ordenar_notas" que use Selection Sort para ordenar una lista de 
calificaciones (enteros, 0 y 100)

notas = [87, 45, 100, 67, 89, 90, 55, 72]
"""

def ordenarNotas(notas):
    count = 0

    for i in range(len(notas) -1):
        print(notas)

        minimum = notas[i] 
        minimum_index = i

        for j in range(i + 1, len(notas)):
            count += 1
            if notas[j] < minimum:
                minimum = notas[j] 
                minimum_index = j

        if minimum_index != i:
            # Intercambiamos el valor minimo encontrado con el valor actual
            notas[minimum_index], notas[i] = notas[i], notas[minimum_index]
    return(f'{notas} \nNumber of comparisons = {count}')

notas = [87, 45, 100, 67, 89, 90, 55, 72]
print(ordenarNotas(notas))


"""
LeetCode
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):

            minimum = nums[i]
            minumum_index = i

            for j in range(i + 1, len(nums)):
                if nums[j] < minimum:
                    minimum = nums[j]
                    minumum_index = j
            
            if minumum_index != i:
                nums[minumum_index], nums[i] = nums[i], nums[minumum_index]

        return nums
        