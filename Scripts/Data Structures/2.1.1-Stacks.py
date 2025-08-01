"""
stack = []

stack.append(1)
stack.append(2)
print(stack.pop())
print(stack[-1])
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


# Creamos la pila como una lista vacia
stack = []

# Agregamos los elementos(push)
stack.append("BMW")
stack.append("Corvette")
stack.append("Lambo")

# Consultamos el tope (peek)
print("Peek: ", stack[-1])

# Eliimnar tope
print("pop: ", stack.pop())

# Agregar elemento
stack.append("Toyota Camri")

# Consultamos el tope nuevamente
print("Peek: ", stack[-1])

