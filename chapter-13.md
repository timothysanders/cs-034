# Chapter 13: Graphs

### 13.1: Graphs - Introduction
#### Introduction to graphs
- A **graph** is a data structure that represents connections among items, and consists of vertices connected by edges.
  - A **vertex** (or node) represents an item in a graph
  - An **edge** represents a connection between two vertices in a graph
#### Adjacency and paths
- In a graph
  - Two vertices are **adjacent** if connected by an edge
  - A **path** is a sequence of edges leading from a source (starting) vertex to a destination (ending) vertex. The **path length** is the number of edges in the path
  - The **distance** between two vertices is the number of edges on the shortest path between those vertices

### 13.2: Applications of graphs
#### Geographic maps and navigation
- Graphs are often used to represent a geographic map, which can contain information about places/travel routes
- Vertices in a graph can represent airports, with edges representing available flights
- Edge weights can be used to represent the length of the travel route, either in total distance or expected time to navigate the route
- Another example is a map service with access to real-time traffic information
#### Product recommendations
- A graph can represent relationships between products. Vertices in the graph corresponding to a customer's purchased products have adjacent vertices representing products that can be recommended
#### Social and professional networks
- A graph may use a vertex to represent a person and an edge in such a graph represents a relationship between two people. In social networks, edges commonly represent friendship, whereas business networks use edges to represent business conducted between two people

### 13.3: Graph representations - Adjacency lists
#### Adjacency lists
- A common approach for representing graph data structures is through an adjacency list. Two vertices are **adjacent** if they are connected by an edge. In an **adjacency list** representation, each vertex has a list of adjacent vertices, with each list item representing an edge
#### Advantages of adjacency lists
- Key advantage of an adjacency list is its size of $O(V + E)$, each vertex appears once and each edge appears twice. V refers to the number of vertices and E is the number of edges
- A disadvantage is that determining whether two vertices are adjacent is $O(V)$, because one vertex's adjacency list must be traversed looking for another vertex, and the list may have V items. In most applications though, a vertex is only adjacent to a small fraction of other vertices, which creates a sparse graph.
- A **sparse graph** has far fewer edges than the maximum possible. Since many graphs are sparse, the adjacency list graph representation is very common

### 13.4: Graph representations - Adjacency matrices
#### Adjacency matrices
- An adjacency matrix can be used for representing a graph data structure. Two vertices are **adjacent** if they are connected by an edge. In an **adjacency matrix** representation, each vertex is assigned to a matrix row and column, and a matrix element is 1 if the corresponding vertices have an edge or is 0 otherwise
#### Analysis of adjacency matrices
- Assuming the implementation of a two-dimensional array whose elements are accessible in $O(1)$, the key benefit of an adjacency matrix is $O(1)$ determination of whether two vertices are adjacent.
- A key drawback is $O(V^2)$ size, and an adjacency matrix's large size is inefficient for a sparse graph, where most elements are 0s.
- An adjacency matrix only represents edges among vertices, it does not represent any data like a person's name or address.

### 13.5: Graphs - Breadth-first search
#### Graph traversal and breadth-first search
- An algorithm must visit every vertex in a graph in some order, which is called a **graph traversal**
- A **breadth-first search** (BFS) is a traversal that visits a starting index, then all vertices of distance 1 from that vertex, then distance 2, etc., without revisiting a vertex. The visiting order of the same-distance vertices does not matter
#### Breadth-first algorithm
- The algorithm enqueues the starting vertex in a queue. While the queue is not empty, the algorithm dequeues a vertex, visits it, enqueues that vertex's adjacent vertices (if not already discovered), then repeats
```text
BFS(start_vertex) {
    ENQUEUE start_vertex IN frontier_queue
    ADD start_vertex TO discovered_set
    
    WHILE (frontier_queue IS NOT EMPTY) {
        current_vertex = DEQUEUE FROM frontier_queue
        visit(current_vertex)
        FOR EACH vertex adj_v ADJACENT TO current_vertex {
            IF (adj_v IS NOT IN discovered_set) {
                ENQUEUE adj_v IN frontier_queue
                ADD adj_v to discovered_set
            }
        }
    }
}
```
- When BFS first encounters a vertex, it is said to have been **discovered**. In the BFS algorithm, vertices in the queue are called the **frontier**, as they are vertices that are discovered but not yet visited. Already discovered vertices are not visited again

### 13.6: Graphs - Depth-first search
#### Graph traversal and depth-first search
- An algorithm must visit every vertex in a graph in some order, this is called **graph traversal**
- A **depth-first search** (DFS) is a traversal that visits a starting vertex, then visits every vertex along each path, starting from the vertex to the path's end before backtracking
#### Depth-first search algorithm
- An algorithm for depth-first search pushes the starting vertex to a stack. While the stack is not empty, the algorithm pops the vertex from the top of the stack. If the vertex has not been visited, the algorithm visits the vertex and pushes adjacent vertices to the stack
```text
DFS(start_vertex) {
    CREATE empty stack vertex_stack
    CREATE empty set visited_set
    
    PUSH start_vertex TO vertex_stack
    WHILE (vertex_stack is not empty) {
        current_v = POP(vertex_stack)
        IF (current_v IS NOT IN visited_set) {
            VISIT(current_v)
            ADD current_v TO visited_set
            FOR EACH vertex adj_v ADJACENT TO current_v {
                PUSH adj_v to vertex_stack
            }
        }
    }
}
```
#### Recursive DFS algorithm
- Recursive DFS can be implemented using the program stack instead of an explicit stack. In the algorithm, if a vertex has not already been visited, the algorithm visits the vertex and performs a recursive DFS call for each adjacent vertex
```text
RecursiveDFS(current_v) {
    IF (current_v IS NOT IN visited_set) {
        ADD current_v TO visited_set
        "Visit" current_v
        FOR EACH vertex adj_v ADJACENT TO current_v {
            RecursiveDFS(adj_v)
        }
    }
}
```

### 13.7: Directed Graphs
#### Directed graphs
- A **directed graph**, or **digraph**, consists of vertices connected by directed edges. A **directed edge** is a connection between a starting vertex and a terminating vertex. In a directed graph, a vertex Y is **adjacent** to vertex X if there is an edge from X to Y (but X is not adjacent to Y). The **degree** of a vertex is the sum of the number of incoming and outgoing edges
#### Paths and cycles
- In a directed graph
  - A **path** is a sequence of directed edges leading from a source (starting) vertex to a destination (ending) vertex
  - A **cycle** is a path that starts and ends at the same vertex. A directed graph is **cyclic** if the graph contains a cycle and **acyclic** if the graph does not contain a cycle

### 13.8: Weighted graphs
#### Weighted graphs
- A **weighted graph** associates a particular weight with each edge. A graph edge's **weight** (or **cost**) represents some numerical value between vertex items. This could be something like flight cost, travel time, etc. Weighted graphs can be directed or undirected
#### Path length in weighted graphs
- In a weighted graph, the **path length** is the sum of the edge weights in the path
- The shortest path is the path that has the lowest sum of edge weights
#### Negative edge weight cycles
- The **cycle length** is the sum of the edge weights in a cycle. A **negative edge weight cycle** has a cycle length less than 0. A shortest path does not exist in a graph with a negative edge weight cycle, because each loop around the negative edge weight further decreases the cycle length, so there is no minimum

### 13.9: Python - Graphs

### 13.12: Python - Dijkstra's shortest path
#### Dijkstra's shortest path
- Dijkstra's algorithm computes the shortest path from a given starting vertex to all other vertices in the graph

### 13.13: Algorithm - Dijkstra's shortest path
#### Dijkstra's shortest path algorithm
- There are many different applications for finding the shortest path between vertices in a graph, such as finding the shortest driving route
- **Dijkstra's shortest path algorithm**, created by Edsger Dijkstra, determines the shortest path from a start vertex to each vertex in the graph. For each vertex, Dijkstra's algorithm determines the vertex's distance and predecessor pointer. A vertex's **distance** is the shortest path distance from the start vertex. A vertex's **predecessor pointer** points to the previous vertex along the shortest path from the start vertex.
- The algorithm initializes all vertices' distances to infinity, all vertices' predecessors to null, and enqueues all vertices into a queue of unvisited vertices. The algorithm assigns the start vertex's distance to 0 and while the queue is not empty, computes the distance of the path from the start vertex to the current vertex, then continuing on to the adjacent vertex. If the path's distance is shorter than the adjacent vertex's current distance, a shorter path has been found. The adjacent vertex's current distance is updated to the distance of the newly found shorter path's distance, and vertex's predecessor pointer is pointed to the current vertex.
#### Finding shortest path from start vertex to destination vertex
- After running Dijkstra's algorithm, the shortest path from the start vertex to the destination vertex can be determined using the vertices' predecessor pointers. If the destination vertex's predecessor pointer is not 0, the shortest path is traversed in reverse by following the predecessor pointers until the start vertex is reached. If the destination vertex's predecessor pointer is null, then a path from the start vertex to the destination vertex does not exist.
#### Negative edge weights
- Dijkstra's shortest path algorithm can be used for unweighted graphs (using a uniform edge weight of 1) and weighted graphs with non-negative edges weights. For a directed graph with negative edge weights, Dijkstra's algorithm may not find the shortest path for some vertices, so the algorithm should not be used if a negative edge weight exists

### 13.14: Algorithm - Bellman-Ford's shortest path
#### Bellman-Ford shortest path algorithm
- The **Bellman-Ford shortest path algorithm** (created by Richard Bellman and Lester Ford, Jr) determines the shortest path from a start vertex to each vertex in a graph. For each vertex, the Bellman-Ford algorithm determines the vertex's distance and predecessor pointer. A vertex's **distance** is the shortest path distance from the start vertex. A vertex's **predecessor pointer** points to the previous vertex along the shortest path from the start vertex.
- The Bellman-Ford algorithm initializes all vertices' current distances to infinity and predecessors to null, and assigns the start vertex with a distance of 0. The algorithm performs V-1 main iterations, visiting each vertex in the graph during each iteration. Each time a vertex is visited, the algorithm follows all edges to adjacent vertices. For each adjacent vertex, the algorithm computes the distance of the path from the start vertex to the current vertex and continuing on to the adjacent vertex. If that path's distance is shorter than the adjacent vertex's current distance, a shorter path has been found. The adjacent vertex's current distance is updated to the newly found shorter path's distance, and the vertex's predecessor pointer is pointed to the current vertex. 
- The Bellman-Ford algorithm does not require a specific order for visiting vertices during the main iteration.
#### Checking for negative edge weight cycles
- The Bellman-Ford algorithm supports graphs with negative edge weights. However, if a negative edge weight cycle exists, a shortest path does not exist. After visiting all vertices V-1 times, the algorithm checks for negative edge weight cycles. If a negative edge weight cycle does not exist, the algorithm returns true (shortest path exists), otherwise false

### 13.16: Topological sort
#### Overview
- A **topological sort** of directed, acyclic graphs produces a list of the graph's vertices such that for every edge from a vertex X to a vertex Y, X comes before Y in the list
- A single graph can have more than one topographical sort ordering, and it does not require weighted edges. A topographical sort's first vertex must have 0 incoming edges, and the last vertex must have 0 outgoing edges
#### Example: course prerequisites
- Graphs can indicate a sequence of steps, where an edge from X to Y indicates that X must be done before Y. A topographical sort of such a graph provides one possible ordering for performing the steps.
#### Topographical sort algorithm
- The algorithm uses three lists: a results list containing the topological sort of vertices, a no-incoming-edges list of vertices with no incoming edges, and a remaining-edges list. The results list starts as an empty list of vertices, the no-incoming-edges vertex list starts as a list of all vertices in the graph with no incoming edges, the remaining-edges list starts as a list of all edges in the graph
- The algorithm executes while the no-incoming-edges vertex list is not empty. For each iteration, a vertex is removed from the no-incoming-edges list and added to the result list. Next, a temporary list is built by removing all edges in the remaining-edges list that are outgoing from the removed vertex. For each edge currentE in the temporary list, the number of edges in the remaining-edges list that are incoming to currentE's terminating vertex are counted. If the incoming edge count is 0, then currentE's terminating vertex is added to the no-incoming-edges vertex list.
- Because each loop iteration can remove any vertex from the no-incoming-edges list, the algorithm's output is not guaranteed to be the graph's only possible topological sort

### 13.17: Python - Topological sort
#### Topological sort algorithm
- The topological sort algorithm finds an ordered list of vertices from a directed graph where no vertex has an outgoing edge to a preceding vertex in the list. Topological sorting is useful in many real-world situations such as manufacturing (where some components must be built before other components) or course scheduling (where some courses must be completed as prerequisites to other courses). When the graph is drawn with the vertices lined up left to right in the order of a topological sort, then all edges will point in the direction from left to right.
#### Iterating through a collection of edges
- The topological sorting algorithm iterates through lists of edges, which we are representing in a 2-tuple form (from_vertex, to_vertex) and a for loop can iterate through a list or set of edges

### 13.8: Minimum spanning tree
#### Overview
- A graph's **minimum spanning tree is a subset of the graph's edges that connect all vertices in the graph together with the minimum sum of edge weights. The graph must be weighted and connected. A **connected** graph contains a path between every pair of vertices
#### Kruskal's minimum spanning tree algorithm
- **Kruskal's minimum spanning tree algorithm** determines the subset of graph edges that connect all the graph's vertices with the minimum possible sum of edge weights. This algorithm uses three collections
  - `edge_queue`: a priority queue of edges, initially containing all graph edges. Edge weights are priorities
  - `results`: a collection of edges comprising the minimum spanning tree, initially empty
  - `vertex_sets`: a collection of vertex sets. Each set represents vertices connected by edges in `result`. Initially, `vertex_sets` contains one set for each vertex
- The algorithm executes while `edge_queue` has at least one edge. In each iteration, the edge with the lowest weight is removed from the edge queue. If the removed edge connects two different vertex sets, then the edge is added to the resulting minimum spanning tree, and the two vertex sets are merged.
- Kruskal's algorithm has a space complexity of $O(|E| + |V|)$. If the edge list is sorted at the beginning, removals are done in constant time, and when combined with a mechanism to map a vertex to the containing vertex set in constant time, the algorithm's runtime complexity is $O(|E|\log|E|)$

### 13.20: All pairs shortest path
#### Overview and shortest paths matrix
- An **all pairs shortest path** algorithm determines the shortest path between all possible pairs of vertices in a graph, using a V x V matrix to represent the shortest path lengths between all vertex pairs. Each row corresponds to a start vertex and each column corresponds to a terminating vertex for each path
- These shortest path matrices only store the path lengths of the shortest path, not the sequence of vertices that make up the path
- The shortest path length from any vertex to itself is 0
#### Floyd-Warshall algorithm
- The **Floyd-Warshall all-pairs shortest path algorithm** generates a V*V matrix of values representing the shortest path lengths between all vertex pairs in a graph. Graphs with cycles and negative edge weights are supported, but you cannot have negative cycles (which are cycles with edge weights that sum to a negative value).
- The Floyd-Warshall algorithm initializes the shortest path lengths matrix using three steps
  1. Every entry assigned with infinity
  2. Each entry representing the path from a vertex to itself is assigned with 0
  3. For each edge from X to Y in the graph, the matrix entry for the path from X to Y is initialized with the edge's weight
- The algorithm then iterates through every vertex in the graph, for each vertex X, the shortest path lengths for all vertex pairs are recomputed by considering X as an intermediate vertex. For each matrix entry representing A to B, existing matrix entries are used to compute the length of the path from A through X to B. If this path is less than the current shortest path, the corresponding matrix entry is updated.
- The Floyd-Warshall algorithm builds a V*V matrix and has a space complexity of $O(V^2)$. The matrix is constructed with a runtime complexity of $O(|V|^3)$