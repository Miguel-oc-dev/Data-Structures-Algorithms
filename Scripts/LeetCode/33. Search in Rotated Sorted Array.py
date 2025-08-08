"""
Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Binary search
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # Calculamos el indice medio del rango actual
            mid = (left + right) // 2
            # Si el valor en el medio es igual al target, se retorna
            if nums[mid] == target:
                return mid
            
            # Empezamos con las verificaciones
            # Verificamos si la mitad izquiera esta ordenada
            if nums[left] <= nums[mid]:
                # Si el target esta fuera del rango ordenado izqujierdo
                if target < nums[left] or target > nums[mid]:
                    # Buscamos en la mitad derecha
                    left = mid + 1
                else:
                    # Buscamos en la mitad izquierda
                    right = mid - 1
            # Lo mismo para la mitad derecha
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return - 1