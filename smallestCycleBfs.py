from collections import deque, defaultdict

def smallest_cycle_bfs(graph):
    """
    Detect the smallest cycle in an undirected graph using BFS.
    
    Args:
        graph: A dictionary representing an adjacency list.
               Example: {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    
    Returns:
        The length of the smallest cycle, or -1 if no cycle exists.
    """
    def bfs(start):
        visited = set()
        queue = deque([(start, -1, 0)])  # (node, parent, path_length)
        visited.add(start)

        while queue:
            node, parent, length = queue.popleft()

            for neighbor in graph[node]:
                if neighbor not in visited:
                    # If neighbor is unvisited, continue BFS
                    visited.add(neighbor)
                    queue.append((neighbor, node, length + 1))
                elif neighbor != parent:
                    # Cycle detected
                    return length + 1  # Add 1 to include the cycle edge
        
        return float('inf')  # No cycle found from this node

    # Try to find the smallest cycle from all nodes
    smallest_cycle = float('inf')

    for node in graph:
        # Perform BFS starting from the current node
        cycle_length = bfs(node)
        smallest_cycle = min(smallest_cycle, cycle_length)

    return smallest_cycle if smallest_cycle != float('inf') else -1
