"""
Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

HashMap para conteo de caracteres
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Convertimos nums1 y nums2 en un conjunto(set) para eliminar duplicados
        nums1 = set(nums1)
        nums2 = set(nums2)

        # Retronamos el resultado en "list" con la oeracion de interseccion "&"
        return list(nums1 & nums2)