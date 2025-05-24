from __future__ import annotations
from vertex import Vertex

class EdgeWeight:
    """
    Implement a weighted edge between two vertices.

    Attributes
    ----------
    from_vertex : Vertex
    to_vertex : Vertex
    weight : float

    Methods
    -------
    __eq__
    __ge__
    __gt__
    __le__
    __lt__
    __ne__
    """
    def __init__(self, from_vertex: Vertex, to_vertex: Vertex, weight: float):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def __eq__(self, other: EdgeWeight) -> bool:
        return self.weight == other.weight

    def __ge__(self, other: EdgeWeight) -> bool:
        return self.weight >= other.weight

    def __gt__(self, other: EdgeWeight) -> bool:
        return self.weight > other.weight

    def __le__(self, other: EdgeWeight) -> bool:
        return self.weight <= other.weight

    def __lt__(self, other: EdgeWeight) -> bool:
        return self.weight < other.weight

    def __ne__(self, other: EdgeWeight) -> bool:
        return self.weight != other.weight