"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true

Two Pointers
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalnum()])
        start_index = 0
        final_index = len(s) - 1

        while start_index < final_index:
            if s[start_index] != s[final_index]:
                return False
            start_index += 1
            final_index -= 1
        return True