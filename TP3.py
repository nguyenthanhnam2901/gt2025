# Directed graph G: {V, E}
# V:    vertices = [1, 2, 3, 4, 5, 6, 7, 8]
# E:    edges = [(1,2),(1,3),(2,5),(2,6),(3,4),(4,8),(5,7)] 

# a) Construct adjacent Matrix for graph G
# b) Write Inoder algo to exploit tree G which obey behavior 
# Input node label (x)
# Print out all node of subtree (x) in (Inorder)

# Part (a): Construct adjacency matrix for the directed graph G
def construct_adjacency_matrix(vertices, edges):
    n = len(vertices)
    adjacency_matrix = [[0] * n for _ in range(n)]
    vertex_to_index = {vertex: i for i, vertex in enumerate(vertices)}

    for u, v in edges:
        adjacency_matrix[vertex_to_index[u]][vertex_to_index[v]] = 1

    return adjacency_matrix

# Part (b): Perform Inorder traversal on tree-like graph
def build_tree_from_edges(edges):
    """
    Builds a binary tree-like structure from the edges.
    Assumes edges describe a tree.
    """
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    nodes = {}

    # Create nodes for all unique vertices
    for u, v in edges:
        if u not in nodes:
            nodes[u] = TreeNode(u)
        if v not in nodes:
            nodes[v] = TreeNode(v)

        # Assign left or right child
        if nodes[u].left is None:
            nodes[u].left = nodes[v]
        else:
            nodes[u].right = nodes[v]

    return nodes

def inorder_traversal(node):
    if node is None:
        return []

    # Recursively traverse left, visit root, then traverse right
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)

# Driver code
def main():
    vertices = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]

    # Part (a): Construct adjacency matrix
    adj_matrix = construct_adjacency_matrix(vertices, edges)
    print("Adjacency Matrix:")
    for row in adj_matrix:
        print(row)

    # Part (b): Perform Inorder Traversal
    nodes = build_tree_from_edges(edges)

    while True:
        try:
            start_node = int(input("Enter the starting node for Inorder traversal: "))
            if start_node not in nodes:
                print("Invalid node label. Please enter a valid node label.")
                continue

            root = nodes[start_node]
            inorder_result = inorder_traversal(root)
            print("\nInorder Traversal Result starting from node {}:".format(start_node))
            print(" ".join(map(str, inorder_result)))
            break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == '__main__':
    main()