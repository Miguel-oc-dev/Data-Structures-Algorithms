"""
Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Boyer-Moore Majority Vote
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = 0 # Candidato al elemento mayoritario
        count = 0 # Contador

        for num in nums:
            if count == 0:
                count += 1 
                target = num # Establece un nuevo candidato
            elif target == num:
                count += 1 # Suma si el numero es igual al candidato actual
            else:
                count -= 1 # Resta si el numero es diferente al candidato

        return target
    
"""
Este algoritmo funciona basándose en cancelaciones:

Cuando encuentras un número igual al candidato, aumentas el contador.
Cuando encuentras un número diferente, lo cancelas restando el contador.

Si el contador llega a cero, significa que la cantidad de elementos distintos al candidato actual lo igualan, 
así que se elige un nuevo candidato.
Dado que el problema garantiza que existe un elemento mayoritario 
(más de la mitad de los elementos del arreglo), este método siempre terminará con el correcto.
"""