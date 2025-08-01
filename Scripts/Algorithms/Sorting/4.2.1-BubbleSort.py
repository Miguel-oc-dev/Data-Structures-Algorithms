"""
Bubble Sort

In this sorting algorithm, the largest value is bubbled up in every pass
Every two adjacent items are compared and they are swapped if they are in the wrong order
After every pass, the largest element reaches to the end of the array

Complexity: O(n^2) - Best case: O(n)
"""

def bubbleSort(array):
    count = 0
    # El "-1" es porque cuando solo quede un elemento, no necesitamos ordenarlo
    for i in range(len(array) - 1):
        print(array)
        # En cada itercion del bucle, se ordena un numero, por lo tanto, el bucle interno solo se ejecutara para la parte no ordenada
        for j in range(len(array) - i - 1):
            count += 1
            # Si dos elementos adjacentes se encuentran en el orden incorrecto, se intercambian 
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return(f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(bubbleSort(array))

"""
Se puede optimizar ligeramente añadiendo una variable que registra si se realizaron
intercambios en la ultima iteracion, ej.
Si por ejemplo a la mitad de los bucles, la matriz se ordena por completo, no haremos comparaciones innecesarias
"""

def optimizedBubbleSort(array):
        count = 0
        for i in range(len(array) - 1):
            swap = False
            print(array)
            for j in range(len(array) - i - 1):
                count += 1
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swap = True
            if swap == False:
                return(f'{array} \nNumber of comparisons = {count}')
                
        return(f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(optimizedBubbleSort(array))


"""
Problema 1
Ordena una lista de cadenas de texto por orden alfabetico
"""

def alfabeticBubbleSort(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array) -i -1):
            count += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return (f'{array} \nNumber of comparisons = {count}')
print(alfabeticBubbleSort(["banana", "apple", "cherry", "date"]))


"""
LeetCode
905. Sort Array By Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n -i -1):
                if nums[j] % 2 != 0 and nums[j + 1] % 2 == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    