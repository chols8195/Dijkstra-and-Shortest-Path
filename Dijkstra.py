from collections import defaultdict

# Graph class to represent a directed graph
# Referenced module 17 slide 16
class Graph:
    def __init__(self):
        # Set of all nodes in the graph
        self.nodes = set()
        # Adjacency list for edges, where each node has a list of outgoing edges
        self.edges = defaultdict(list)
        # Dictionary to store distances between nodes, used for edge weights
        self.distances = {}

    # Add a node to the graph
    def add_node(self, value):
        self.nodes.add(value)

    # Add a directed edge with a weight
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


# Dijkstra's algorithm to compute the shortest paths from a start node
def dijkstra(graph, start):
    # Dictionary to store the shortest distance from the start node to each node
    visited = {start: 0}
    # Dictionary to store the path (i.e., predecessor of each node)
    path = {}
    # Set of unvisited nodes
    nodes = set(graph.nodes)

    print("Starting Dijkstra's algorithm...\n--------------------------------\n")
    
    # Loop until all nodes have been visited or there are no nodes to visit
    while nodes:
        # Find the node with the smallest distance from the visited nodes
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None or visited[node] < visited[min_node]:
                    min_node = node

        # If no node can be selected, exit the loop (this means there are no connected nodes left)
        if min_node is None:
            break

        # Remove the selected node from unvisited nodes
        nodes.remove(min_node)
        current_weight = visited[min_node]
        print(f"Node({min_node}) with Weight: {current_weight} is added to the 'Visited' {list(visited.keys())}")

        # Check all neighboring nodes of the selected node
        for neighbor in graph.edges[min_node]:
            # Calculate the new distance (current node's distance + edge weight)
            weight = current_weight + graph.distances[(min_node, neighbor)]
            
            # Relaxation step: Update distance if a shorter path is found
            if neighbor not in visited or weight < visited[neighbor]:
                print(f"Relaxed: vertex[{neighbor}]: OLD: {visited.get(neighbor, 'Infinity')}, NEW: {weight}, PATHS: {path}")
                visited[neighbor] = weight  # Update shortest distance for the neighbor
                path[neighbor] = min_node   # Update the predecessor of the neighbor (i.e., the current node)
            else:
                print(f"No edge relaxation is needed for node [{neighbor}]\n")

    # Return the shortest distances and paths
    return visited, path


def main():
    # Constructing the Graph
    ConstructGraph = Graph()
    # List of nodes to add to the graph
    nodes = ['s', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 't']
    for node in nodes:
        ConstructGraph.add_node(node)

    # List of edges (from_node, to_node, distance)
    edges = [
        ('s', 'A', 1), ('s', 'D', 4), ('s', 'G', 6),
        ('A', 'B', 2), ('A', 'D', 3), ('A', 'E', 2),
        ('B', 'C', 2), ('C', 'E', 2), ('C', 'F', 1), ('C', 't', 4),
        ('D', 'E', 3), ('D', 'G', 2), ('E', 'F', 3), ('E', 'G', 1),
        ('E', 'H', 2), ('E', 'I', 3), ('F', 'I', 1), ('F', 't', 3),
        ('G', 'H', 6), ('H', 'I', 6), ('I', 't', 4)
    ]
    for from_node, to_node, distance in edges:
        ConstructGraph.add_edge(from_node, to_node, distance)

    # Running Dijkstra's Algorithm from the start node 's'
    visited, path = dijkstra(ConstructGraph, 's')

    # Displaying Final Results
    print("\nFinal Shortest Path Results: \n----------------------------")
    
    # Display the shortest distance to each visited node
    print("Visited (Shortest Distances):")
    for node, distance in visited.items():
        print(f"  {node}: {distance}")

    # Display the predecessor of each node, showing the path from the start node
    print("\nPath (Predecessors):")
    for node, predecessor in path.items():
        print(f"  {node}: {predecessor}")
    
    # Calculate the total weight of all the shortest paths
    total_weight = 0
    for node, distance in visited.items():
        total_weight += distance
    print(f"Total Weight: {total_weight}")    

# Entry point of the script
if __name__ == "__main__":
    main()
