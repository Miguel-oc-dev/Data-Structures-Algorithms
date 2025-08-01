"""
Grafos
"""

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Depth-First Search (DFS)
def dfs(grafo, nodo, visitados = None):
    if visitados is None:
        visitados = set()
    print(nodo, end = ' ')
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
            

# Breadth-First Search (BFS)
from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(nodo, end = ' ')
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("DFS desde A:")
dfs(grafo, 'A')
print("\nBFS desde A:")
bfs(grafo, 'A')