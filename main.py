from operator import itemgetter
import matplotlib.pyplot as plt

class DisjointSet:
    def __init__(self, ids):
        self.id = ids

    def find(self, x):
        while x != self.id[x]:
            x = self.id[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.id[x] = y

def plot_mst(mst):
    for src, dst, _ in mst:
        x, y = [points[src][1], points[dst][1]], [points[src][2], points[dst][2]]
        plt.plot(x, y, marker='o', mfc='red', mec='red', color='black')
    plt.show()

def euclidean(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5

def create_graph(points):
    graph = {}
    for src, xsrc, ysrc in points:
        for dst, xdst, ydst in points:
            if src == dst: continue
            if dst > src: break
            if src not in graph:
                graph[src] = {}
            if dst not in graph:
                graph[dst] = {}
            weight = euclidean((xsrc, ysrc), (xdst, ydst))
            graph[src][dst] = weight
            graph[dst][src] = weight
    return graph

def read_input(datafile, classfile):
    points = []
    with open(datafile, 'r') as f:
        for i, line in enumerate(f.readlines()):
            x, y = list(map(float,line.split()))
            points.append((i, x, y))
    
    classes = []
    with open(classfile, 'r') as f:
        for i, line in enumerate(f.readlines()):
            classes.append((i, int(line)))
    
    return points, classes

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



def kruskal(graph):
    mst = []
    ds = DisjointSet(list(graph.keys()))
    edges = graph_to_edges(graph)
    edges = sorted(edges, key=itemgetter(2))
    for src, dst, weight in edges:
        if ds.find(src) != ds.find(dst):
            mst.append((src, dst, weight))
            ds.union(src, dst)
    return mst

def prim(graph):
    return


def find_clusters(classes, graph):
    cluster_id = 0
    vertices = list(graph.keys())
    

    while vertices:
        start = vertices.pop()

        classes[start] = cluster_id
        visited, stack = set(), [start]
        while stack:
            v = stack.pop()
            if v in visited: continue
            
            visited.add(v)

            if v != start:
                classes[v] = cluster_id
                vertices.remove(v)
            
            for adj in graph[v]:
                if adj in visited: continue
                stack.append(adj)

        cluster_id += 1
    
    return classes, cluster_id

def clustering(graph, k, algorithm):
    algorithms = {'kruskal': kruskal, 'prim': prim}
    if algorithm not in algorithms:
        raise ValueError("Invalid algorithm")

    classes = [-1] * len(graph)
    mst = algorithms[algorithm](graph)

    while True:
        classes, nclusters = find_clusters(classes, edges_to_graph(mst))
        if nclusters == k: break
        print(mst.pop())

    return classes

points, classes = read_input('data.txt', 'classes.txt')
graph = create_graph(points)
# mst = kruskal(graph)
# plot_mst(mst)

# colormap = {
#     0:'black',
#     1:'green',
#     2:'blue',
#     3:'red',
#     4:'purple',
#     5:'gray',
#     6:'yellow'
# }
# for i, c in enumerate(clustering(graph, 7, 'kruskal')):
#     i, x, y = points[i]
#     plt.plot(x,y,'o', markersize=2, color=colormap[c])
# plt.show()