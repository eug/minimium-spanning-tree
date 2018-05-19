from utils import euclidean

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

