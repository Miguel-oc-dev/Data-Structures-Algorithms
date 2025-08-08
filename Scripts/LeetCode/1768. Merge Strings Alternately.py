"""
Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
tarting with word1. If a string is longer than the other, append the additional letters onto the end 
of the merged string.
Return the merged string.

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []
        word = 1

        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            elif word == 2:
                s.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            s.append(word1[a])
            a += 1

        while b < B:
            s.append(word2[b])
            b += 1

        return ''.join(s)
