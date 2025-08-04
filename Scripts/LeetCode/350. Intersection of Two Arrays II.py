"""
Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Two Pointers
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Ordenamos ambos arreglos
        nums1.sort()
        nums2.sort()

        # Inicializamos dos punteros para recorrer las listas
        left = 0
        right = 0

        # Lista para almacenar los elementos
        map = []

        # Recorremos ambos arrays mientras no lleguemos al final de alguno
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]: # Si el elemento en nums1 es menor, avaza el puntero
                left += 1
            elif nums2[right] < nums1[left]: # Si el elemento en nums2 es menor, avanza el puntero
                right += 1
            else:
                # Si ambos elementos son iguales, se agrega al resultado y avanzan ambos punteros
                map.append(nums1[left])
                left += 1
                right += 1
        return map