"""
Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Queues
"""


from collections import deque

class MyStack:
    def __init__(self):
        # Creamos una cola vacía usando deque
        self.queue = deque()

    def push(self, x: int) -> None:
        # Agregamos el nuevo elemento al final de la cola
        self.queue.append(x)
        # Rotamos la cola para que el nuevo elemento quede al frente
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # Quitamos y devolvemos el primer elemento (LIFO)
        return self.queue.popleft()

    def top(self) -> int:
        # Devolvemos el primer elemento sin eliminarlo
        return self.queue[0]

    def empty(self) -> bool:
        # Verificamos si la cola está vacía
        return not self.queue
