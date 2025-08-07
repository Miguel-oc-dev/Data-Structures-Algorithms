"""
Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1

Fast & Slow Pointers
"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Inicializamos dos punteros: slow y fast, ambos empiezan en la cabeza de la lista
        fast, slow = head, head

        # Esta primera parte es para detectar si hay un ciclo en la lista
        while fast and fast.next:
            slow = slow.next         # Avanza de uno en uno
            fast = fast.next.next    # Avanza de dos en dos

            # Si se encuentran, significa que hay un ciclo
            if slow == fast:
                # Para encontrar el nodo de inicio del ciclo:
                # Colocamos uno de los punteros (slow) al inicio de la lista
                slow = head

                # Avanzamos ambos punteros de uno en uno hasta que se encuentren
                # El nodo donde se encuentran es el inicio del ciclo
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow  # Este es el nodo donde inicia el ciclo

        # Si no hay ciclo, retornamos None
        return None
