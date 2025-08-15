#!/usr/bin/env python3
"""
Smart Traffic Route Optimizer (Python)
Readable, beginner-friendly implementation.

Features:
 - Graph using adjacency lists
 - Node coordinates (for A* heuristic)
 - Dijkstra's algorithm (shortest-path)
 - A* algorithm (optional faster search with Euclidean heuristic)
 - Path reconstruction and simple CLI demo map
"""

from dataclasses import dataclass
from typing import List, Tuple
import heapq
import math

# ----- Data structures -----
@dataclass
class Edge:
    to: int
    weight: float  # travel time or distance

@dataclass
class Node:
    id: int
    x: float
    y: float
    name: str

class Graph:
    def __init__(self, reserve: int = 0):
        self.nodes: List[Node] = []
        self.adj: List[List[Edge]] = []

    def add_node(self, name: str, x: float, y: float) -> int:
        node_id = len(self.nodes)
        self.nodes.append(Node(node_id, x, y, name))
        self.adj.append([])
        return node_id

    def add_edge(self, u: int, v: int, w: float, bidir: bool = True) -> None:
        self._ensure_node(u)
        self._ensure_node(v)
        self.adj[u].append(Edge(v, w))
        if bidir:
            self.adj[v].append(Edge(u, w))

    def neighbors(self, u: int) -> List[Edge]:
        return self.adj[u]

    def get_node(self, i: int) -> Node:
        return self.nodes[i]

    def size(self) -> int:
        return len(self.nodes)

    def _ensure_node(self, i: int) -> None:
        if i < 0 or i >= len(self.nodes):
            raise IndexError("node id out of range")


# ----- Utilities -----
def euclidean(a: Node, b: Node) -> float:
    """Euclidean distance used as A* heuristic"""
    return math.hypot(a.x - b.x, a.y - b.y)


# ----- Dijkstra -----
def dijkstra(g: Graph, src: int) -> Tuple[List[float], List[int]]:
    n = g.size()
    INF = math.inf
    dist = [INF] * n
    parent = [-1] * n

    # min-heap of (distance, node)
    heap = []
    dist[src] = 0.0
    heapq.heappush(heap, (0.0, src))

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # stale entry
        for e in g.neighbors(u):
            v = e.to
            nd = d + e.weight
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(heap, (nd, v))

    return dist, parent


# ----- A* -----
def astar(g: Graph, src: int, dst: int) -> Tuple[List[float], List[int]]:
    n = g.size()
    INF = math.inf
    gscore = [INF] * n  # cost from start to node
    fscore = [INF] * n  # g + heuristic
    parent = [-1] * n

    def heur(u: int) -> float:
        return euclidean(g.get_node(u), g.get_node(dst))

    open_heap: List[Tuple[float, int]] = []
    gscore[src] = 0.0
    fscore[src] = heur(src)
    heapq.heappush(open_heap, (fscore[src], src))

    while open_heap:
        f, u = heapq.heappop(open_heap)
        # If we pop the destination, we found the best path to it
        if u == dst:
            break
        if f > fscore[u]:
            continue  # stale

        for e in g.neighbors(u):
            v = e.to
            tentative = gscore[u] + e.weight
            if tentative < gscore[v]:
                parent[v] = u
                gscore[v] = tentative
                fscore[v] = tentative + heur(v)
                heapq.heappush(open_heap, (fscore[v], v))

    return gscore, parent


# ----- Path reconstruction -----
def reconstruct_path(parent: List[int], src: int, dst: int) -> List[int]:
    path: List[int] = []
    cur = dst
    while cur != -1:
        path.append(cur)
        if cur == src:
            break
        cur = parent[cur]
    path.reverse()
    if not path or path[0] != src:
        return []  # no path
    return path


def print_path(g: Graph, path: List[int], dist: float) -> None:
    if not path:
        print("No path found.")
        return
    names = " -> ".join(g.get_node(i).name for i in path)
    print(f"Path: {names}")
    print(f"Total cost: {dist}")


# ----- Sample map -----
def sample_map() -> Graph:
    g = Graph()
    # Add nodes: name, x, y
    A = g.add_node("A:Station", 0.0, 0.0)
    B = g.add_node("B:Market", 2.0, 1.0)
    C = g.add_node("C:College", 4.0, 0.0)
    D = g.add_node("D:Hospital", 1.0, -2.0)
    E = g.add_node("E:Mall", 3.0, -2.0)
    F = g.add_node("F:Airport", 6.0, -1.0)

    # Add edges (bidirectional by default)
    g.add_edge(A, B, 2.2)
    g.add_edge(A, D, 2.5)
    g.add_edge(B, C, 2.5)
    g.add_edge(B, E, 3.0)
    g.add_edge(C, F, 2.8)
    g.add_edge(D, E, 1.8)
    g.add_edge(E, F, 3.0)
    g.add_edge(B, D, 3.4)

    return g
