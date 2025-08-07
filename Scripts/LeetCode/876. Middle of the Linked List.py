"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]

Fast & Slow Pointers
"""

# Definicioon del nodo de la lista
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # Valor almacenado en el nodo
        self.next = next # Referencia al siguiente nodo

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Se recorre la lista cuando el puntero rapido no llegue al final
        # Y el nodo siguiente a fast no sea None
        while fast is not None and fast.next is not None:
            slow = slow.next # Avanza de uno en uno
            fast = fast.next.next # Avanza de dos en dos
        return slow
        # Cuando el bucle termina, fast ha llegado (o “saltado”) al final

