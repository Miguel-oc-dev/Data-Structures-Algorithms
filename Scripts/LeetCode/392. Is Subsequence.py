"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence 
of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Definimos dos punteros con la posicion incial para cada cadena
        # S recorre s, lo que vamos a buscar
        # T recorre t, en donde lo vamos a buscar
        S, T = 0, 0

        # Recorremos ambas cadenas mientras no lleguemos al final de alguna
        while S < len(s) and T < len(t):
            # Si el caracter actual de s es igual al de t
            if s[S] == t[T]:
                # Avanza el puntero para seguir buscando en s
                S += 1
            # Siempre avanzamos T para seguir buscando en t
            T += 1
        # Si S llego al final de s, encontramos toda la subsecuencia
        return S == len(s)