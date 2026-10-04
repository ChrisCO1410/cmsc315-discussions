"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # Edge case: Return empty list if graph is empty or start node is not in the graph
    if not graph or start not in graph:
        return []

    # A queue (FIFO - First-In-First-Out) is used to explore nodes level-by-level.
    # Nodes that are discovered first are processed first, ensuring all nodes at
    # distance d are processed before nodes at distance d + 1.
    queue = deque([start])

    # A visited set is essential to avoid processing the same node multiple times,
    # which prevents infinite loops in graphs with cycles.
    visited = {start}

    # Stores the final order of node visits
    traversal_order = []

    while queue:
        # Pop the front element from the queue (FIFO behavior)
        current = queue.popleft()
        traversal_order.append(current)

        # Explore all adjacent neighbors of the current node
        for neighbor in graph.get(current, []):
            # Neighbors are added to the queue as soon as they are discovered.
            # This guarantees that we explore the immediate connections (Level 1)
            # before moving on to deeper connections (Level 2, Level 3, etc.).
            # Unlike DFS (Depth-First Search), which uses a stack/recursion to dive
            # as deep as possible down a single path, BFS spreads outward evenly.
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def print_graph(graph):
    """Helper function to display the graph adjacency list cleanly."""
    for node, neighbors in graph.items():
        print(f"  Node '{node}' connects to -> {neighbors}")


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")

    # Graph Representation: Adjacency List using a Python Dictionary
    # Real-World Scenario: Streaming Platform User Connection / Preference Network
    # Nodes represent users or content hubs (User A, User B, etc.).
    # Edges (connections) represent direct mutual connections or shared viewing interests.
    graph = {
        'User_A': ['User_B', 'User_C'],
        'User_B': ['User_A', 'User_D', 'User_E'],
        'User_C': ['User_A', 'User_F'],
        'User_D': ['User_B'],
        'User_E': ['User_B', 'User_F'],
        'User_F': ['User_C', 'User_E']
    }

    print("Initial Graph (Adjacency List):")
    print_graph(graph)

    # Explanation of Adjacency List representation
    print("\nExplanation of Graph Structure:")
    print("  - Representation: Adjacency List implemented using Python dictionary keys and lists.")
    print("  - Vertices/Nodes: 6 users ('User_A' through 'User_F').")
    print("  - Edges: Connections showing direct mutual friend/content relationships.")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    start_node = 'User_A'
    order = bfs(graph, start_node)
    print(f"Starting BFS Traversal from: {start_node}")
    print(f"Traversal Result Order: {' -> '.join(order)}")

    print("\nStep-by-Step Level-by-Level Breakdown:")
    print("  Level 0 (Start): ['User_A']")
    print("  Level 1 (Direct Friends of A): ['User_B', 'User_C']")
    print("  Level 2 (Friends of Level 1): ['User_D', 'User_E', 'User_F']")

    # Modifying Graph: Adding an additional node ('User_G') and connection from 'User_D'
    print("\n-- Modifying Graph: Adding Node 'User_G' and Edge 'User_D' -> 'User_G' --")
    graph['User_D'].append('User_G')
    graph['User_G'] = ['User_D']

    print_graph(graph)

    updated_order = bfs(graph, start_node)
    print(f"\nUpdated BFS Traversal Order from {start_node}:")
    print(f"  {' -> '.join(updated_order)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Start from a different starting node
    print("\n1. Edge Case: Starting from a different node ('User_F')")
    order_f = bfs(graph, 'User_F')
    print(f"   Traversal Order: {' -> '.join(order_f)}")
    print("   Explanation: Traversal reorganizes naturally starting at User_F's immediate level 1 neighbors.")

    # Edge Case 2: Missing / Non-existent start node
    print("\n2. Edge Case: Missing start node ('User_Z')")
    order_missing = bfs(graph, 'User_Z')
    print(f"   Traversal Order: {order_missing}")
    print("   Explanation: Safely returns an empty list without throwing a KeyError.")

    # Edge Case 3: Disconnected Graph Component
    print("\n3. Edge Case: Disconnected graph component")
    disconnected_graph = {
        'Node_1': ['Node_2'],
        'Node_2': ['Node_1'],
        'Node_3': []  # Isolated node
    }
    order_disc = bfs(disconnected_graph, 'Node_1')
    print(f"   Traversal Order from Node_1: {' -> '.join(order_disc)}")
    print("   Explanation: BFS only visits nodes in the connected component reachable from the start node.")


if __name__ == "__main__":
    main()