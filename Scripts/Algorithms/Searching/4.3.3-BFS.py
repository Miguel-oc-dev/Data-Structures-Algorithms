class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def BFS(root):
    queue = []
    queue.append(root)

    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            print(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

BFS(root)