from heapq import heappush, heappop
import math
from utils import edges_to_graph, graph_to_edges, DisjointSet
from operator import itemgetter

def _find_clusters(mst_graph, vertices):
    classes = [-1] * len(vertices)
    vertices = vertices.copy()        
    cluster_id = 0
    
    while vertices:
        start = vertices.pop()
        classes[start] = cluster_id
        visited, stack = set(), [start]

        while stack:
            v = stack.pop()

            if v in visited:
                continue
            
            if v != start:
                vertices.remove(v)

            visited.add(v)
            classes[v] = cluster_id

            if v not in mst_graph:
                continue

            for adj in mst_graph[v]:
                if adj in visited: continue
                stack.append(adj)

        cluster_id += 1
    
    return classes, cluster_id

class Kruskal:
    @staticmethod
    def mst(graph):
        if not graph or not isinstance(graph, dict):
            raise ValueError("graph must be a dict.")
        return Kruskal._algorithm(graph, k=0)

    @staticmethod
    def clustering(graph, k):
        if not graph or not isinstance(graph, dict):
            raise ValueError("graph must be a dict.")
        if not k or k <= 0:
            raise ValueError("k must be greater than 0.")
        return Kruskal._algorithm(graph, k)

    @staticmethod
    def _algorithm(graph, k):
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
        if not graph or not isinstance(graph, dict):
            raise ValueError("graph must be a dict.")
        return Prim._algorithm(graph)

    @staticmethod
    def clustering(graph, k):
        if not graph or not isinstance(graph, dict):
            raise ValueError("graph must be a dict.")
        if not k or k <= 0:
            raise ValueError("k must be greater than 0.")

        
        mst = Prim._algorithm(graph)
        vertices = [v for v in graph]

        while True:
            _graph = edges_to_graph(mst)
            classes, nclusters = _find_clusters(_graph, vertices)
            if nclusters == k: break
            mst.pop()

        return classes

    @staticmethod
    def _algorithm(graph):
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
