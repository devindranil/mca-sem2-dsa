# DFS Traversal in Graph without using class

# Graph represented using dictionary
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [],
    4: [],
    5: [],
    6: []
}

# DFS Function
def dfs(graph, node, visited):

    # Mark node as visited
    visited.add(node)

    print(node, end=" ")

    # Visit adjacent nodes
    for neighbour in graph[node]:

        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# Driver Code
visited = set()

print("DFS Traversal:")

dfs(graph, 0, visited)