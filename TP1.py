# Req: Impl Path_existance 
# and test check for graph in Pref Prog
# Langue where they following behavior;

# 1) As user input 2 node
# 2) Return True if path exist else False

def path_existence(graph, start, end):
    """
    Check if a path exists between two nodes in the graph.

    Parameters:
    graph (dict): Adjacency list representing the graph.
    start (int): Starting node.
    end (int): Ending node.

    Returns:
    bool: True if a path exists, False otherwise.
    """
    visited = set()

    def dfs(node):
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(start)

def build_graph(vertices, edges):
    """
    Build an adjacency list graph from vertices and edges.

    Parameters:
    vertices (list): List of vertices.
    edges (list of tuples): List of edges (tuples of two vertices).

    Returns:
    dict: Adjacency list representation of the graph.
    """
    graph = {v: [] for v in vertices}
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)  # undirected graph 
    return graph

def main():
    vertices = [1, 2, 3, 4, 5, 6, 7]
    edges = [(1, 2), (2, 5), (3, 6), (4, 6), (4, 7), (6, 7)]
    graph = build_graph(vertices, edges)

    # Test Cases
    print(path_existence(graph, 1, 5))  # True
    print(path_existence(graph, 1, 7))  # False
    print(path_existence(graph, 3, 7))  # True
    print(path_existence(graph, 5, 4))  # False

if __name__ == "__main__":
    main()