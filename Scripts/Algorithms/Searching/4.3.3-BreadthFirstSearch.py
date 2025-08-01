"""
Breadth First Search
Is a traversal algorithm for tree or graph, where we start the root node
And visit all the nodes level from left to right. It requires us to keep track 
Complexity: O(n)

To implement BFS, we'll need a Binary Search Tree. So we'll use that
"""

# Clase que representa cada nodo del árbol
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
# Arbol Binario de Busqueda
class BST:
    def __init__(self):
        self.root = None
        self.numberOfNodes = 0
    
    # Inserta un nuevo nodo en el arbol
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.numberOfNodes += 1
            return
        
        current = self.root
        
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            
            else:
                break
        self.numberOfNodes += 1
    
    # Busca un valor en el arbol
    def search(self, data):
        current = self.root
        
        while current:
            if data == current.data:
                return "Found"
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return "Not Found"
    
    # Metodo BFS iterativo
    def BFS(self):
        if self.root is None:
            return "Tree is empty"

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.data)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    
    # Metodo BFS recursivo
    def recursiveBFS(self, queue, result):
        if self.root is None:
            return "Tree is empty"
        if not queue:
            return result
        
        current = queue.pop(0)
        result.append(current.data)

        if current.left:
                queue.append(current.left)
        if current.right:
                queue.append(current.right)
        return self.recursiveBFS(queue, result)

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(13)
tree.insert(65)
tree.insert(0)
tree.insert(10)

print("BFS Iterativo: ", tree.BFS())
print("BFS Recursivo: ", tree.recursiveBFS([tree.root], []))