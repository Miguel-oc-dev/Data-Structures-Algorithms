"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Creamos un nodo "dummy" que sera usado como punto de partida de una nueva lista
        dummy = ListNode()
        tail = dummy

        # Mientras ambas listas tengan nodos por comparar
        while list1 and list2:
            # Comparamos los valores de los nodos actuales de list1 y list2
            if list1.val < list2.val:
                # Si el valor de list1 es menor, se agrega ese nodo a la lista 
                tail.next = list1
                list1 = list1.next # Avanzamos al siguiente nodo
            else:
                tail.next = list2 # Lo mismo que en el caso contrario
                list2 = list2.next
            
            # Avanzamos el tail para que siempre apunte al ultimo nodo
            tail = tail.next

        # Si alguno de las dos listas aun tiene nodos, los agregamos al final
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Retornamos el siguiente nodo, que es el inicio real de la nueva lista fusionada
        return dummy.next