# Give the directed graph as a matrix represent 
#     G = [
#         [0, 1, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 1, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 1, 0, 0, 0, 1],
#         [0, 0, 1, 1, 0, 0, 0, 0, 0],
#         [0, 0, 1, 0, 1, 1, 0, 1, 0],
#         [0, 0, 1, 0, 0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     ]

#     vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     edges = [(1, 2), (1, 4), (2, 6), (2, 3), (5, 4), (5, 9), (5, 5), (6, 4), (6, 3), (7, 3), (7, 5), (7, 6), (7, 8), (8, 3), (8, 9)]

# Return number of weakly connected component and strongly connected component 


from collections import defaultdict

def matrix_to_edges(matrix):
    """
    Convert adjacency matrix to edge list.
    """
    edges = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                edges.append((i + 1, j + 1))
    return edges

def build_graph(vertices, edges):
    """
    Build a directed graph as an adjacency list.
    """
    graph = {v: [] for v in vertices}
    for edge in edges:
        u, v = edge
        graph[u].append(v)
    return graph

def reverse_graph(graph):
    """
    Reverse the edges of the graph.
    """
    reversed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    return reversed_graph

def dfs(graph, node, visited, stack=None):
    """
    Perform a DFS on the graph.
    """
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    if stack is not None:
        stack.append(node)

def kosaraju_scc(graph):
    """
    Kosaraju's Algorithm to find the number of strongly connected components (SCCs).
    """
    # Perform DFS and track the finish time in a stack
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)

    # Reverse the graph
    reversed_graph = reverse_graph(graph)

    # Perform DFS on the reversed graph in the order of decreasing finish time
    visited.clear()
    scc_count = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            dfs(reversed_graph, node, visited)
            scc_count += 1

    return scc_count

def weakly_connected_components(vertices, edges):
    """
    Find the number of weakly connected components by treating the graph as undirected.
    """
    # Build an undirected graph
    graph = defaultdict(list)
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)  # Treat as undirected

    visited = set()
    wcc_count = 0

    for node in vertices:
        if node not in visited:
            dfs(graph, node, visited)
            wcc_count += 1

    return wcc_count

def main():
    # Directed graph adjacency matrix
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    vertices = list(range(1, len(G) + 1))
    edges = matrix_to_edges(G)

    # Input vertices and edges
    # vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # edges = [(1, 2), (1, 4), (2, 6), (2, 3), (5, 4), (5, 9), (5, 5), (6, 4), (6, 3), (7, 3), (7, 5), (7, 6), (7, 8), (8, 3), (8, 9)]

    # Build the graph
    graph = build_graph(vertices, edges)

    # Count SCCs
    scc_count = kosaraju_scc(graph)

    # Count WCCs
    wcc_count = weakly_connected_components(vertices, edges)

    print(f"Number of Strongly Connected Components (SCCs): {scc_count}")
    print(f"Number of Weakly Connected Components (WCCs): {wcc_count}")

if __name__ == "__main__":
    main()
