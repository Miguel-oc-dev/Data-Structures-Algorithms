"""
Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Two Pointers
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Inicialiozamos los dos punteros
        start_index, final_index = 0, len(s) - 1

        while start_index < final_index:
            # Se intercambian las posiciones de inicio a final
            s[start_index], s[final_index] = s[final_index], s[start_index]

            # Avanzan los punteros hacia el centro
            start_index += 1
            final_index -= 1
        