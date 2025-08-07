"""
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Two Pointers
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Inicializamos tres punteros:
        # pointer_n1: apunta al último elemento válido en nums1
        pointer_n1 = m - 1
        # pointer_n2: apunta al último elemento en nums2
        pointer_n2 = n - 1
        # position: apunta al final de nums1 (donde hay espacio suficiente para ambos arrays)
        position = m + n - 1

        # Mientras aún queden elementos en nums2 por insertar
        while pointer_n2 >= 0:
            # Si aún hay elementos válidos en nums1 y el actual de nums1 es mayor que el actual de nums2
            if pointer_n1 >= 0 and nums1[pointer_n1] > nums2[pointer_n2]:
                # Coloca el valor más grande en la posición final de nums1
                nums1[position] = nums1[pointer_n1]
                # Mueve el puntero de nums1 hacia la izquierda
                pointer_n1 -= 1
            else:
                # Si el valor actual de nums2 es mayor o nums1 ya no tiene elementos válidos,
                # coloca el de nums2 en la posición final
                nums1[position] = nums2[pointer_n2]
                # Mueve el puntero de nums2 hacia la izquierda
                pointer_n2 -= 1
            # Avanza a la siguiente posición desde el final
            position -= 1
