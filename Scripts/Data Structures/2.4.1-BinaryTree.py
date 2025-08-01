"""
Binary tree
"""

class Nodo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """
    Recorridos del arbol

    Inorden	Izquierdo → Raíz → Derecho
    Preorden	Raíz → Izquierdo → Derecho
    Postorden	Izquierdo → Derecho → Raíz
    """

def inorden(nodo):
    if nodo:
        inorden(nodo.left)
        print(nodo.value, end = ' ')
        inorden(nodo.right)

def preorden(nodo):
    if nodo:
        print(nodo.value, end = ' ')
        preorden(nodo.left)
        preorden(nodo.right)

def postorden(nodo):
    if nodo:
        postorden(nodo.left)
        postorden(nodo.right)
        print(nodo.value, end = '')


root = Nodo(10)
root.left = Nodo(5)
root.right = Nodo(15)
root.right.right = Nodo(12)
root.right.left = Nodo(20)
        
print("Root: ", root.value)
print("Left child: ", root.left.value)
print("Right child: ", root.right.value)

# Recorridos
print("Recorrido inorden:")
inorden(root)
print("\nRecorrido preorden:")
preorden(root)
print("\nRecorrido postorden:")
postorden(root)


# Segundo arbol
class Nodo2:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add_recursive(current, value):
    if current is None:
        return Nodo2(value)

    if value < current.value:
        current.left = add_recursive(current.left, value)
    elif value > current.value:
        current.right = add_recursive(current.right, value)
    else:
        return current
    return current

def contains_node_recursive(current, value):
    if current is None:
        return False
    if value == current.value:
        return True
    
    if value < current.value:
        return contains_node_recursive(current.left, value)
    else:
        return contains_node_recursive(current.right, value)
    
def inorder_travesal(nodo2):
    if nodo2 is not None:
        inorder_travesal(nodo2.left)
        print(nodo2.value)
        inorder_travesal(nodo2.right)


# Crear raiz y agregar nodos
root2 = Nodo2(10)

root2 = add_recursive(root2, 10)
root2 = add_recursive(root2, 5)
root2 = add_recursive(root2, 15)
root2 = add_recursive(root2, 3)
root2 = add_recursive(root2, 8)

# Imprimir recorrido in order
print("In order travesal of the tree: ")
inorder_travesal(root2)

# Buscar valores
print("Contiene 15? ", contains_node_recursive(root2, 15))
print("Contiene 42? ", contains_node_recursive(root2, 42))