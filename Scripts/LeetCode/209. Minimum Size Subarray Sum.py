"""
Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Slicing Window
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_length = float('inf')

        # Recorrido del arreglo con el puntero derecho
        for right in range(len(nums)):
            # Añadimos el valor actual al total de la ventana
            total += nums[right]

            # Mientras el total de la ventana sea mayor o igual
            while total >= target:
                # Actualizamos la longitud minima si encontramos una ventana mas pequeña
                min_length = min(min_length, right - left + 1)
                
                # Restamos el valor del extremo izq y movemos la ventana a la derecha
                total -= nums[left]
                left += 1
                
        # Si no encontramos ninguna subarreglo que cumpla la condición, devolvemos 0
        return 0 if min_length == float('inf') else min_length