"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Input: s = "abcabcbb"
Output: 3

Slicing Window (Dynamic)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Conjunto para rastrear los caracteres unicos en la ventana
        char_set = set()
        # Puntero inicial
        left = 0
        # Longitud maxima encontrada
        max_length = 0

        # Recorremos con el puntero derecho
        for right in range(len(s)):
            # Si el caracter actual ya esta en el conjunto, se reduce la ventana
            while s[right] in char_set:
                # Elimina el caracter duplicado
                char_set.remove(s[left])
                left += 1

            # Agregamos el caracter actual a la ventana
            char_set.add(s[right])

            # Calculamos la longitud de la ventana actual y actualizamos la maxima
            max_length = max(max_length, right - left + 1)
        return max_length