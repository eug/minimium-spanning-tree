import math
from heapq import heappop, heappush
from operator import itemgetter

from utils import DisjointSet, edges_to_graph, graph_to_edges


def _find_clusters(mst_graph, vertices):
    """Find the cluster class for each vertex of the MST graph.
    It uses the DFS-like algorithm to find clusters.
    
    Args:
        mst_graph (dict): A non-empty graph representing the MST.
        vertices (list): A list of unique vertices.
    
    Returns:
        A list containing the group id of each vertex.
    """
    cluster_id = 0
    classes = [-1] * len(vertices)
    unexplored = vertices.copy()        
    
    while unexplored:
        start = vertices.pop()
        classes[start] = cluster_id
        explored, stack = set(), [start]

        while stack:
            v = stack.pop()

            if v in explored:
                continue

            if v != start:
                unexplored.remove(v)

            explored.add(v)
            classes[v] = cluster_id

            if v not in mst_graph:
                continue

            for adj in mst_graph[v]:
                if adj in explored: continue
                stack.append(adj)

        cluster_id += 1

    return classes, cluster_id

class Kruskal:

    @staticmethod
    def mst(graph):
        """Find the Minimum Spanning Tree of a given graph.

        Args:
            graph (dict): A non-empty graph.
        
        Returns:
            list: Returns a list of tuples representing the edges of the graph.
        """
        if not graph or not isinstance(graph, dict):
            raise ValueError("graph must be a dict.")
        return Kruskal._algorithm(graph, k=0)

    @staticmethod
    def clustering(graph, k):
        """Find k clusters in a given graph.
        The clustering algorithm uses Kruskal's algorithm to find the MST,
        during the Kruskal execution when the number of groups in the 
        Disjoint-Set matches with k, then the algorithm stops and returns 
        the group of each vertex.
        
        Args:
            graph (dict): A non-empty graph.
            k (int): Number of clusters.
        
        Returns:
            list: Returns a list containing the group id of each vertex.
        """
        if not graph or not isinstance(graph, dict):
            raise ValueError("graph must be a dict.")
        if not k or k <= 0:
            raise ValueError("k must be greater than 0.")
        return Kruskal._algorithm(graph, k)

    @staticmethod
    def _algorithm(graph, k):
        """Kruskal's algorithm implementation. It stops the execution
        when the number of groups is equals to k, when k > 0.
        
        Args:
            graph (dict): A non-empty graph.
            k (int): Number of clusters
        
        Returns:
            list: When k > 0, returns a list containing the group id of
                  each vertex. Otherwise, returns a list of tuples 
                  representing the edges of the MST.
        """
        mst = []
        ds = DisjointSet(list(graph.keys()))
        edges = graph_to_edges(graph)
        edges = sorted(edges, key=itemgetter(2))
        for src, dst, weight in edges:
            if ds.find(src) != ds.find(dst):
                mst.append((src, dst, weight))
                ds.union(src, dst)
                if k > 0 and k == ds.ngroups:
                    _graph = edges_to_graph(mst)
                    vertices = [v for v in graph]
                    return next(iter(_find_clusters(_graph, vertices)))
        return mst


class Prim:
    @staticmethod
    def mst(graph):
        """Find the Minimum Spanning Tree of a given graph.

        Args:
            graph (dict): A non-empty graph

        Returns:
            list: Returns a list of tuples representing the edges of the graph.
        """
        if not graph or not isinstance(graph, dict):
            raise ValueError("graph must be a dict.")
        return Prim._algorithm(graph)

    @staticmethod
    def clustering(graph, k):
        """Find k clusters in a given graph.
        The clustering algorithm uses Prim's algorithm to find the MST,
        after the algorithm find the MST, it removes the most distant
        edge from the MST until it finds k clusters in the graph.

        Args:
            graph (dict): A non-empty graph.
            k (int): Number of clusters

        Returns:
            list: Returns a list containing the group id of each vertex.
        """
        if not graph or not isinstance(graph, dict):
            raise ValueError("graph must be a dict.")
        if not k or k <= 0:
            raise ValueError("k must be greater than 0.")
        
        mst = Prim._algorithm(graph)
        mst = sorted(mst, key=itemgetter(2))
        vertices = [v for v in graph]

        while True:
            _graph = edges_to_graph(mst)
            classes, nclusters = _find_clusters(_graph, vertices)
            if nclusters == k: break
            mst.pop()

        return classes

    @staticmethod
    def _algorithm(graph):
        """Prim's algorithm implementation.

        Args:
            graph (dict): A non-empty graph.
            k (int): Number of clusters

        Returns:
            list: Returns a list of tuples representing the edges of the MST.
        """
        mst = []
        start = next(iter(graph))
        explored = []
        unexplored = [(0, start, None)]
        while unexplored:
            w, u, v = heappop(unexplored)
            if u in explored:
                continue
            if not v is None:
                mst.append((v, u, w))
            explored.append(u)
            for n in graph[u]:
                if n not in explored:
                    heappush(unexplored, (graph[u][n], n, u))
        return mst
