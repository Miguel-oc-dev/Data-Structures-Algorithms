from collections import deque

queue = deque()

queue.append("a")
queue.append("b")
print(queue.popleft())
print(queue[0])

class Queue:
    def __init__(self, item):
        self.queue = deque()

    def enqueue(self, item):
        self.items.append(item)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def dequeue(self):
        return self.queue.popleft()
    
    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return not self.queue
    

# Inicializamos la cola como una lista vacia
queue2 = deque()

queue2.append("apple")
queue2.append("banana")
queue2.append("cherry")

print("Queue: ", queue2)  

# Elimina el primer elemento 
front = queue2.popleft()
print("Removed element: ", front)

# Visualiza la cola despues de la eliminacion
print("Queue after removal: ", queue2)  

# Agrega otro elemento
queue2.append("date")

# Ver el elemento al frente sin eliminar
peeked = queue2[0]
print("Peeked element: ", peeked)  

# Visualiamos la cola actualizada
print("Queue after peek: ", queue2)  



