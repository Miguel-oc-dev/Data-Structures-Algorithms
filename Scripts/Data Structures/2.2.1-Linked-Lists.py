"""
Linked List

Es una estructura de datos lineal donde cada elemento(nodo) contiene
    Valor
    Referencia al siguiente nodo

En una list, los elementos están contiguos en memoria. 
En una Linked List, cada nodo apunta al siguiente, lo que permite crecer dinámicamente sin necesidad de mover otros elementos.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def esta_vacia(self):
        return self.cabeza is None
    
    # Insertar al inicio
    def insertar_al_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Insertar al final
    def insertar_al_final(self, valor):
        nuevo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    # Eliminar un nodo (por valor)
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False
    
    # Buscar un valor
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False


    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end = " -> ")
            actual = actual.siguiente

        print("None")


lista = ListaEnlazada()
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.insertar_al_inicio(30)
lista.imprimir()  # 30 -> 20 -> 10 -> None

lista.insertar_al_final(50)
lista.insertar_al_final(60)
lista.insertar_al_final(70)
lista.imprimir()

lista.eliminar(10)
lista.imprimir()

print(lista.buscar(30))



class ListNode:
    def __init__(self, valor, next = None):
        self.valor = valor
        self.next = next

l4 = ListNode("Messi", None)
l3 = ListNode("Steph Curry", l4)
l2 = ListNode("Renaldo", l3)
l1 = ListNode("Michael Jordan", l2)

temp = l1

l5 = ListNode("Garnett", None)

print("Recorriendo la lista enlazada: ")
# Insertar al final de la linked list
while temp:
    if temp.next is None:
        temp.next = l5
        break
    temp = temp.next

print("Insertamos a Garnet al final")
actual = l1
while actual:
    print(actual.valor)
    actual = actual.next

l4.next = None

# Insertar indice despues de MJ
garnett_node = ListNode("Garnett", None)

temp = l1
while temp:
    if temp.valor == "Michael Jordan":
        garnett_node.next = temp.next
        temp.next = garnett_node
        break
    temp = temp.next


print("Insertamos a Garnet despues de Michael Jordan")
actual = l1
while actual:
    print(actual.valor)
    actual = actual.next