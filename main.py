import getopt
import sys
from io import (read_input, save_clusters_png, save_clusters_txt, save_mst_png,
                save_mst_txt)

import matplotlib.pyplot as plt

from algorithms import Kruskal, Prim
from utils import DisjointSet, create_graph, edges_to_graph, graph_to_edges


class Config:
    data_file = None
    class_file = None
    output_type = None
    mode_mst = False
    mode_clustering = False
    kclusters = 0


def parse_args(argv):
    shortopts = 'd:c:k:o:mh'

    longopts = [
        'datafile='
        'classfile=',
        'min-span-tree=',
        'k-clusters=',
        'output-type=',
        'help'
    ]

    config = Config()
    options, _ = getopt.getopt(sys.argv[1:], shortopts, longopts)

    for opt, arg in options:
        if opt in ('-d', '--datafile'):
            config.data_file = arg
        elif opt in ('-c', '--classfile'):
            config.class_file = arg
        elif opt in ('-m', '--min-span-tree'):
            config.mode_mst = True
        elif opt in ('-k', '--k-clusters'):
            config.mode_clustering = True
            config.kclusters = int(arg)
        elif opt in ('-o', '--output-type'):
            if arg in ('txt', 'png'):
                config.output_type = arg
        elif opt in ('-h', '--help'):
            config.show_help = True
    
    return config


def print_help():
    print("""Clustering algorithms using Minimium Spanning Tree.
Usage:
    python main.py -d data.txt -c classes.txt -k 7 -o png
    python main.py -d data.txt -c classes.txt -m -o txt

Options:
    -d --datafile=FILE          Data points file
    -c --classfile=FILE         Classes file
    -m --min-span-tree          Find the MST
    -k --k-clusters=N           Find k clusters
    -o --output-type=png|txt    Specify the output type
    -h --help                   Print this message
    """)

if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print('Missing arguments.')
        sys.exit(1)

    cfg = parse_args(sys.argv[1:])
    points, classes, graph = None, None, None

    if cfg.show_help:
        print_help()
        sys.exit(0)

    if not cfg.data_file:
        sys.stderr.write('Missing datafile argument.\n')
        sys.exit(1)
    
    if not cfg.class_file:
        sys.stderr.write('Missing classfile argument.\n')
        sys.exit(1)

    if not cfg.mode_mst and not cfg.mode_clustering:
        sys.stderr.write('No mode specified.\n')
        sys.exit(1)
    
    if not cfg.output_type:
        sys.stderr.write('Missing output type argument.\n')
        sys.exit(1)

    try:
        points, classes = read_input('data.txt', 'classes.txt')
    except:
        sys.stderr.write('Unable to read input files.\n')
        sys.exit(1)

    graph = create_graph(points)

    if cfg.mode_mst:
        mst_kruskal = Kruskal.mst(graph)
        mst_prim = Prim.mst(graph)
        if cfg.output_type == 'txt':
            save_mst_txt('mst_kruskal.txt', mst_kruskal)
            save_mst_txt('mst_prim.txt', mst_prim)
        elif cfg.output_type == 'img':
            save_mst_png('mst_kruskal.png', mst_kruskal, points)
            save_mst_png('mst_prim.png', mst_prim, points)
    elif cfg.mode_clustering:
        clusters_kruskal = Kruskal.clustering(graph, cfg.kclusters)
        clusters_prim = Prim.clustering(graph, cfg.kclusters)
        if cfg.output_type == 'txt':
            save_clusters_txt('clusters_kruskal.txt', mst_kruskal)
            save_clusters_txt('clusters_prim.txt', mst_prim)
        elif cfg.output_type == 'img':
            save_clusters_png('clusters_kruskal.png', mst_kruskal, points)
            save_clusters_png('clusters_prim.png', mst_prim, points)


















# def plot_mst(points, mst):
#     for src, dst, _ in mst:
#         x, y = [points[src][1], points[dst][1]], [points[src][2], points[dst][2]]
#         plt.plot(x, y, marker='o', mfc='red', mec='red', color='black')
#     plt.show()





# graph = {
#     0: {1: 4, 2: 6, 3: 16},
#     1: {0: 4, 5: 24},
#     2: {0: 6, 3: 8, 4: 5, 6: 23},
#     3: {0: 16, 2: 8, 4:10, 7: 21},
#     4: {2: 5, 3: 10, 5: 18, 6: 11, 7: 14},
#     5: {1: 24, 2: 23, 4: 18, 6: 9},
#     6: {4: 11, 5: 9, 7: 7},
#     7: {3: 21, 4: 14, 6: 7}
# }


# print(Prim.clustering(graph, 4))
# print(Kruskal.clustering(graph, 4))

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

# for i, c in enumerate(Kruskal.clustering(graph, 7)):
#     i, x, y = points[i]
#     plt.plot(x,y,'o', markersize=2, color=colormap[c])
# plt.show()


# for i, c in enumerate(Prim.clustering(graph, 7)):
#     i, x, y = points[i]
#     plt.plot(x,y,'o', markersize=2, color=colormap[c])
# plt.show()
