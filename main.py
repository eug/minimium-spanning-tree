
import matplotlib.pyplot as plt
from heapq import heappush, heappop
import math
from utils import edges_to_graph, graph_to_edges, DisjointSet
from algorithms import Prim, Kruskal

def plot_mst(points, mst):
    for src, dst, _ in mst:
        x, y = [points[src][1], points[dst][1]], [points[src][2], points[dst][2]]
        plt.plot(x, y, marker='o', mfc='red', mec='red', color='black')
    plt.show()


#points, classes = read_input('data.txt', 'classes.txt')
#graph = create_graph(points)

graph = {
    0: {1: 4, 2: 6, 3: 16},
    1: {0: 4, 5: 24},
    2: {0: 6, 3: 8, 4: 5, 6: 23},
    3: {0: 16, 2: 8, 4:10, 7: 21},
    4: {2: 5, 3: 10, 5: 18, 6: 11, 7: 14},
    5: {1: 24, 2: 23, 4: 18, 6: 9},
    6: {4: 11, 5: 9, 7: 7},
    7: {3: 21, 4: 14, 6: 7}
}
print(Prim.mst(graph))
print(Kruskal.mst(graph))

print(Prim.clustering(graph, 4))
print(Kruskal.clustering(graph, 4))

#plot_mst(mst)

# colormap = {
#     0:'black',
#     1:'green',
#     2:'blue',
#     3:'red',
#     4:'purple',
#     5:'gray',
#     6:'yellow'
# }
# for i, c in enumerate(Prim.clustering(graph, 7)):
#     i, x, y = points[i]
#     plt.plot(x,y,'o', markersize=2, color=colormap[c])
# plt.show()