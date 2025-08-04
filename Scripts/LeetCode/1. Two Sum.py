"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

HashMap
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Diccionario (HashMap) para guardar los valores ya vistos
        map = {}

        # Recorremos la lista de numeros
        for i in range(len(nums)):
            # Complemento que necesitamos para el target
            complemento = target - nums[i]
            # Verificamos si ese complemento ya fue visto
            if complemento in map:
                # Si si, devolvemos los indices
                return map[complemento], i
            # Si no, se guarda el numero actual en el diccionario
            map[nums[i]] = i
        return i