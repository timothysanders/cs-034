import queue
import heapq
import itertools

from vertex import Vertex


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def breadth_first_search(self, start_vertex: Vertex) -> (list, dict):
        """
        Conduct a breadth first search (BFS) from the given starting vertex.

        Parameters
        ----------
        start_vertex : Vertex

        Returns
        -------
        visited_list : list
            The order of vertices visited during BFS
        distances : dict
            Mapping from Vertex to distance from start_vertex
        """
        distances = {}
        discovered_set = set()
        frontier_queue = queue.SimpleQueue()
        visited_list = []

        distances[start_vertex] = 0

        frontier_queue.put(start_vertex)
        discovered_set.add(start_vertex)

        while not frontier_queue.empty():
            current_vertex = frontier_queue.get()
            visited_list.append(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in discovered_set:
                    frontier_queue.put(adjacent_vertex)
                    discovered_set.add(adjacent_vertex)
                    distances[adjacent_vertex] = distances[current_vertex] + 1
        return visited_list, distances

    def depth_first_search(self, start_vertex: Vertex, visit_function) -> list[Vertex]:
        """
        Conduct a depth first search (DFS) from the given starting vertex.

        Parameters
        ----------
        start_vertex : Vertex
            - The vertex to start DFS from
        visit_function

        Returns
        -------
        order : list[Vertex]
            - The order of the visited vertices
        """
        if start_vertex not in self.adjacency_list:
            raise ValueError(f"{start_vertex} is not in the graph")
        vertex_stack = [start_vertex]
        visited_set = set()
        order = []

        while vertex_stack:
            current_vertex = vertex_stack.pop()
            if current_vertex not in visited_set:
                visit_function(current_vertex)
                order.append(current_vertex)
                visited_set.add(current_vertex)
                for adjacent_vertex in reversed(self.adjacency_list[current_vertex]):
                    vertex_stack.append(adjacent_vertex)

        return order

    def dijkstra_shortest_path(self, start_vertex: Vertex) -> tuple[dict, dict]:
        """
        Compute shortest-path distances and predecessors from start_vertex using Dijkstra's algorithm.

        A counter is implemented using itertools to act as a tie-breaker in instances where Vertices are
        compared with equal distances.

        Parameters
        ----------
        start_vertex : Vertex
            The vertex from which to compute the shortest paths.

        Returns
        -------
        distances : dict[Vertex, float]
            Mapping of each vertex to its distance from start_vertex.
        predecessors : dict[Vertex, Vertex]
            Mapping of each vertex to its predecessor on the shortest path.
        """
        distances = {v: float('inf') for v in self.adjacency_list}
        predecessors = {v: None for v in self.adjacency_list}
        distances[start_vertex] = 0
        counter = itertools.count()

        heap: list[tuple[float, int, Vertex]] = [(0, next(counter), start_vertex)]
        while heap:
            current_distance, _, u = heapq.heappop(heap)
            if current_distance > distances[u]:
                continue
            for v in self.adjacency_list[u]:
                weight = self.edge_weights.get((u, v), 1.0)
                alt = current_distance + weight
                if alt < distances[v]:
                    distances[v] = alt
                    predecessors[v] = u
                    heapq.heappush(heap, (alt, next(counter), v))

        return distances, predecessors

    def get_shortest_path(self, start_vertex: Vertex, end_vertex: Vertex) -> (list, float):
        """
        Calculate the shortest path between start_vertex and end_vertex.

        Parameters
        ----------
        start_vertex : Vertex
            Starting vertex
        end_vertex : Vertex
            Destination vertex

        Returns
        -------
        path : list
            A list of vertices representing the shortest path from start to end
        total_distance : float
            Total distance of the shortest path
        """
        distances, predecessors = self.dijkstra_shortest_path(start_vertex)

        if distances[end_vertex] == float('inf'):
            return [], float('inf')

        path = []
        current = end_vertex
        while current is not None:
            path.append(current.label)
            current = predecessors[current]

        path.reverse()
        return path, distances[end_vertex]

    def bellman_ford(self, start_vertex: Vertex):
        """
        Compute shortest-path distances and predecessors from start_vertex using the Bellman-Ford algorithm.

        Parameters
        ----------
        start_vertex : Vertex

        Returns
        -------

        """
        for current_vertex in self.adjacency_list:
            current


if __name__ == "__main__":
    g = Graph()
    vertex_a = Vertex("New York")
    vertex_b = Vertex("Tokyo")
    vertex_c = Vertex("London")

    g.add_vertex(vertex_a)
    g.add_vertex(vertex_b)
    g.add_vertex(vertex_c)

    g.depth_first_search(vertex_a, visit_function = lambda v: print(v.label))

    g = Graph()

    vertex_a = Vertex("A")
    vertex_b = Vertex("B")
    vertex_c = Vertex("C")
    vertex_d = Vertex("D")
    vertex_e = Vertex("E")
    vertex_f = Vertex("F")
    vertex_g = Vertex("G")
    g.add_vertex(vertex_a)
    g.add_vertex(vertex_b)
    g.add_vertex(vertex_c)
    g.add_vertex(vertex_d)
    g.add_vertex(vertex_e)
    g.add_vertex(vertex_f)
    g.add_vertex(vertex_g)

    g.add_undirected_edge(vertex_a, vertex_b, 8)
    g.add_undirected_edge(vertex_a, vertex_c, 7)
    g.add_undirected_edge(vertex_a, vertex_d, 3)
    g.add_undirected_edge(vertex_b, vertex_e, 6)
    g.add_undirected_edge(vertex_c, vertex_d, 1)
    g.add_undirected_edge(vertex_c, vertex_e, 2)
    g.add_undirected_edge(vertex_d, vertex_f, 15)
    g.add_undirected_edge(vertex_d, vertex_g, 12)
    g.add_undirected_edge(vertex_e, vertex_f, 4)
    g.add_undirected_edge(vertex_f, vertex_g, 1)
    print(g.get_shortest_path(vertex_a, vertex_f))
    print(g.get_shortest_path(vertex_f, vertex_a))