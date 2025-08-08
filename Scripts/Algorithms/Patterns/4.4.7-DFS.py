def dfs(node, visited):
    if node in visited:
        return

    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor, visited)

#  Arbol binario

def dfs_tree(root):
    if not root:
        return

    # Preorder logic
    dfs_tree(root.left)
    dfs_tree(root.right)
