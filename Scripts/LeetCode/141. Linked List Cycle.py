"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

"""

# Este problema se puede soluciar de dos maneras
# Definimos el nodo de la lista enlazada
class ListNode:
    def __init__(self, x):
        self.val = x # Nodo
        self.next = None # Puntero al siguiente nodo

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Usamos un conjunto para almacenar los nodos ya visitados
        visited = set()

        # Recorremos la vista nodo por nodo
        while head:
            # Si vimos este nodo, hay ciclo
            if head in visited:
                return True
            # De lo contrario, se agrega al conjunto
            visited.add(head)
            # Avanzamos al siguiente nodo
            head = head.next
        return False


# Usando Fast & Slow Pointers
class ListNode:
    def __init__(self, value=0, next= None):
        self.value = value 
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head # Puntero lento, se mueve de uno en uno
        fast = head # Puntero rapido, se mueve de dos en dos

        # Mientras fast y fast.next no sean None, se sigue recorriendo
        while fast and fast.next:
            slow = slow.next # Avanza un paso
            fast = fast.next.next # Avanza dos pasos

            # Si ambos punteros se encuentran, hay un ciclo
            if slow == fast:
                return True
        return False