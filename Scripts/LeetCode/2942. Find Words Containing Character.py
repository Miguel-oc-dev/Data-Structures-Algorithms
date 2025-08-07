"""
Find Words Containing Character

You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.

Input: words = ["leet","code"], x = "e"
Output: [0,1]
"""

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        letter = [] # Lista para guardar los indices

        for index in range(len(words)): # Recorremos la lista con indices
            if x in words[index]: # Si la letra x esta en la palabra
                letter.append(index) # Guardamos el indice
        return letter
