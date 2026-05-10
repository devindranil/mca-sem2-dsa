# BFS Traversal in Graph without using class

from collections import deque

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

# BFS Function
def bfs(graph, start):

    visited = set()      # Store visited nodes
    queue = deque()      # Queue for BFS

    # Start from source node
    queue.append(start)
    visited.add(start)

    print("BFS Traversal:")

    # Traverse graph
    while queue:

        # Remove front node
        node = queue.popleft()

        print(node, end=" ")

        # Visit adjacent nodes
        for neighbour in graph[node]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Driver Code
bfs(graph, 0)