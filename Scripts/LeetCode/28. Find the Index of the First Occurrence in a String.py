"""
Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Caso base: si haystack es más corto que needle, nunca puede contenerlo
        if len(haystack) < len(needle):
            return -1
        
        # Recorremos haystack desde el índice 0 hasta el final
        for i in range(len(haystack)):
            # Tomamos una subcadena del mismo tamaño que needle
            # Empezando desde la posición i
            if haystack[i:i + len(needle)] == needle:
                # Si la subcadena coincide con needle, retornamos el índice i
                return i

        # Si no encontramos ninguna coincidencia después de recorrer haystack
        return -1
