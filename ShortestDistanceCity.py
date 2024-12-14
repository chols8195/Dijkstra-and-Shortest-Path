import sys  # Library for INT_MAX
from collections import defaultdict

# #########################
#
#  Graph class
#
# #########################
class Graph:
    def __init__(self):
        self.nodes = set()  # A set to store all nodes (cities) in the graph
        self.edges = defaultdict(list)  # Adjacency list to store edges
        self.distances = {}  # Dictionary to store distances between nodes

    def add_node(self, value):
        """Add a node (city) to the graph."""
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        """Add an edge (road) between two nodes with a specific distance."""
        self.edges[from_node].append(to_node)  # Directed edge from 'from_node' to 'to_node'
        self.distances[(from_node, to_node)] = distance  # Distance between the two nodes

    def initializeDistances(self):
        """Initialize all distances between nodes to infinity (for MST)."""
        for i in self.nodes:
            for j in self.nodes:
                self.distances[(i, j)] = sys.maxsize  # Set to max size for all pairs

            self.distances[(i, "")] = 0  # Distance from any node to itself is 0

##### End of Graph class #####

# #########################
#
#  Dijkstra's SSSP
#
# #########################
def dijkstra_city_distance(graph, s):
    """Implement Dijkstra's algorithm to find the shortest paths from source `s`."""
    visited = {s: 0}  # Dictionary to store shortest distances from source
    path = dict.fromkeys(graph.nodes, "")  # Dictionary to store paths to nodes

    nodes = set(graph.nodes)  # All nodes in the graph

    # Process nodes until all have been visited
    while nodes:
        min_node = None
        # Find the node with the smallest distance from the visited nodes
        for node in nodes:
            if node in visited:
                if min_node is None or visited[node] < visited[min_node]:
                    min_node = node

        # If there are no reachable nodes, break
        if min_node is None:
            break

        nodes.remove(min_node)  # Remove the processed node from the set
        current_weight = visited[min_node]  # Current shortest distance to `min_node`

        # Display the shortest path to `min_node`
        pathString = ""
        currentCity = min_node

        # Construct the path string
        if path[currentCity] == "":
            path[currentCity] = currentCity
        while path[currentCity] != currentCity:
            pathString = ' to ' + currentCity + pathString
            currentCity = path[currentCity]

        pathString = s + pathString
        print(f'Distance from {s} to {min_node}: {visited[min_node]} with path ({pathString})')

        # Relaxation step - update distances and paths for neighbors
        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, v)]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                path[v] = min_node

    return visited, path

# #########################
#
#  MST
#
# #########################
def printMST(parent, g):
    #print the header for table
    print ("\n\tEdge\t\tWeight\n----------------------------------")
    total = 0  # Total weight of the MST
    #iterate through parent 
    for i in parent.keys():
        #if i = root
        if (parent[i] == "") :
            #print 0 as the node and the distance
            print(f"{i:>15} {i:>15} {g.distances[(i, parent[i])]:.>20d}")
            
        elif(parent[i] != ""):
            total += g.distances[(i, parent[i])]
            print(f"{i:>15} {i:>15} {g.distances[(i, parent[i])]:.>20d}")
            
        else:
            #print the parent node, current node, and the distance
            print(f"{parent[i]:>15} {i:>15} {g.distances[(i, parent[i])]:.>20d}")
    print("\nTotal MST: ", "\t", total)

def minKey(g, key, mstSet):
    """Find the node with the smallest key value that is not yet included in MST."""
    min = sys.maxsize
    min_index = None

    for v in g.nodes:
        if key[v] < min and not mstSet[v]:
            min = key[v]
            min_index = v

    # Print the selected node and its key value
    if min_index is not None:
        print(f'{min_index} is selected. Distance: {min}')

    return min_index

def primMST(graph, s):
    """Implement Prim's algorithm to find the MST of the graph."""
    key = dict.fromkeys(graph.nodes, sys.maxsize)  # Key values used to pick minimum weight edge
    parent = dict.fromkeys(graph.nodes, None)  # Array to store the constructed MST

    key[s] = 0  # Start from the source node
    mstSet = dict.fromkeys(graph.nodes, False)  # Track nodes included in MST

    parent[s] = ""  # Root node of MST

    for aNode in graph.nodes:
        u = minKey(graph, key, mstSet)  # Pick the minimum key vertex

        mstSet[u] = True  # Mark the picked vertex as processed

        # Update key and parent for adjacent vertices
        for v in graph.nodes:
            if (graph.distances[(u, v)] > 0 and mstSet[v] == False and key[v] > graph.distances[(u,v)]):
                key[v] = graph.distances[(u, v)]
                parent[v] = u
    printMST(parent, graph)

def main():
    """Main function to set up the graph and run Dijkstra's and Prim's algorithms."""
    g = Graph()
    #set up nodes
    g.add_node('Atlanta')
    g.add_node('Boston')
    g.add_node('Chicago')
    g.add_node('Dallas')
    g.add_node('Denver')
    g.add_node('Houston')
    g.add_node('LA')
    g.add_node('Memphis')
    g.add_node('Miami')
    g.add_node('NY')
    g.add_node('Philadelphia')
    g.add_node('Phoenix')
    g.add_node('SF')
    g.add_node('Seattle')
    g.add_node('Washington')

    #set up edges for Prim's algrithm
    g.initializeDistances()

    #set up distances (edges)
    g.add_edge('Seattle', 'SF', 1092)
    g.add_edge('SF','Seattle',  1092)
    g.add_edge('Seattle', 'LA', 1544)
    g.add_edge('LA', 'Seattle', 1544)
    g.add_edge('LA', 'SF', 559)
    g.add_edge('SF', 'LA', 559)
    g.add_edge('LA', 'Houston', 2205)
    g.add_edge('Houston', 'LA', 2205)
    g.add_edge('LA', 'Denver', 1335)
    g.add_edge('Denver', 'LA', 1335)
    g.add_edge('LA', 'NY', 3933)
    g.add_edge('NY', 'LA', 3933)
    g.add_edge('LA', 'Miami', 3755)
    g.add_edge('Miami', 'LA', 3755)
    g.add_edge('Denver', 'Dallas', 1064)
    g.add_edge('Dallas', 'Denver', 1064)
    g.add_edge('Denver', 'Boston', 2839)
    g.add_edge('Boston', 'Denver', 2839)
    g.add_edge('Denver', 'Memphis', 1411)
    g.add_edge('Memphis', 'Denver', 1411)
    g.add_edge('Denver', 'Chicago', 1474)
    g.add_edge('Chicago', 'Denver', 1474)
    g.add_edge('Chicago', 'Boston', 1367)
    g.add_edge('Boston', 'Chicago', 1367)
    g.add_edge('Chicago', 'NY', 1145)
    g.add_edge('NY', 'Chicago', 1145)
    g.add_edge('Boston', 'NY', 306)
    g.add_edge('NY', 'Boston', 306)
    g.add_edge('Boston', 'Atlanta', 1505)
    g.add_edge('Atlanta', 'Boston', 1505)
    g.add_edge('Atlanta', 'Dallas', 1157)
    g.add_edge('Dallas', 'Atlanta', 1157)
    g.add_edge('Dallas', 'Houston', 362)
    g.add_edge('Houston', 'Dallas', 362)
    g.add_edge('Atlanta', 'Miami', 973)
    g.add_edge('Miami', 'Atlanta', 973)
    g.add_edge('Atlanta', 'SF', 3434)
    g.add_edge('SF', 'Atlanta', 3434)
    g.add_edge('Dallas', 'Memphis', 675)
    g.add_edge('Memphis', 'Dallas', 675)
    g.add_edge('Memphis', 'Philadelphia', 1413)
    g.add_edge('Philadelphia', 'Memphis', 1413)
    g.add_edge('Miami', 'Phoenix', 3182)
    g.add_edge('Phoenix', 'Miami', 3182)
    g.add_edge('Miami', 'Washington', 1487)
    g.add_edge('Washington', 'Miami', 1487)
    g.add_edge('Phoenix', 'NY', 3441)
    g.add_edge('NY', 'Phoenix', 3441)
    g.add_edge('Phoenix', 'Chicago', 2332)
    g.add_edge('Chicago', 'Phoenix', 2332)
    g.add_edge('Phoenix', 'Dallas', 1422)
    g.add_edge('Dallas', 'Phoenix', 1422)
    g.add_edge('Philadelphia', 'Washington', 199)
    g.add_edge('Washington', 'Philadelphia', 199)
    g.add_edge('Philadelphia', 'Phoenix', 3342)
    g.add_edge('Phoenix', 'Philadelphia', 3342)
    g.add_edge('Washington', 'Dallas', 1900)
    g.add_edge('Dallas', 'Washington', 1900)
    g.add_edge('Washington', 'Denver', 2395)
    g.add_edge('Denver', 'Washington', 2395)

    print("\nDijkstra's Algorithm Results: \n-----------------------------------------------------")
    dijkstra_city_distance(g, 'Denver')
    print("\n\nPrim's Algorithm Results: \n-----------------------------------------------------")
    primMST(g, 'Denver')

if __name__ == "__main__":
    main()
