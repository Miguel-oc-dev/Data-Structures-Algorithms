"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # Nodo previo
        curr = head # Nodo actual, comienza la cabeza

        while curr:     # Mientras no sea None
            next_node = curr.next   # Guarda el siguiente nodo
            curr.next = prev        # Invierte el puntero del nodo actual
            prev = curr             # Avanza puntero prev
            curr = next_node        # Avanza puntero curr
        return prev