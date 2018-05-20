from utils import euclidean

def read_input(datafile, classfile):
    """Read the data points file and class id of each point.

    Args:
        datafile (str): Data points file.
        classfile (str): Point class file.
    
    Returns:
        tuple: Returns a tuple containing a list of points and a list
               containing the class of each point.
    """
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

def save_mst_txt(filename, edges):
    pass

def save_mst_png(filename, edges, points):
    pass

def save_clusters_txt(filename, classes):
    pass

def save_clusters_png(filename, classes, points):
    pass