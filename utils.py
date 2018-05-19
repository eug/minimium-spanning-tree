
class DisjointSet:
    def __init__(self, ids):
        self.id = ids
        self.ngroups = len(self.id)

    def find(self, x):
        while x != self.id[x]:
            x = self.id[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.id[x] = y
            self.ngroups -= 1
            

def graph_to_edges(graph):
    return [(src, dst, graph[src][dst]) for src in graph for dst in graph[src]]

def edges_to_graph(edges):
    graph = {}
    for src, dst, weight in edges:
        if src not in graph:
            graph[src] = {}
        if dst not in graph:
            graph[dst] = {}
        graph[src][dst] = weight
        graph[dst][src] = weight
    return graph


def euclidean(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5
