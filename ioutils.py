from utils import euclidean
import matplotlib.pyplot as plt

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
    """Save MST into a text file.

    Args:
        filename (str): Output filename.
        edges (list): List of tuple representing edges as (src, dst, weight).
    """
    with open(filename, 'w') as f:
        for src, dst, weight in edges:
            f.write('{},{},{}\n'.format(src, dst, weight))

def save_mst_png(filename, edges, points):
    """Save MST into a png file.

    Args:
        filename (str): Output filename.
        edges (list): List of tuple representing edges as (src, dst, weight).
        poits(list): List of tuple representing points as (x, y).
    """
    for src, dst, _ in edges:
        x, y = [points[src][1], points[dst][1]], [points[src][2], points[dst][2]]
        plt.plot(x, y, marker='o', ms=3, mfc='red', mec='red', color='black')
    
    plt.savefig(filename, dpi=300)

def save_clusters_txt(filename, classes):
    """Save clusters into a text file.

    Args:
        filename (str): Output filename.
        classes (list): Class of each data point.
    """
    with open(filename, 'w') as f:
        for _class in classes:
            f.write('{}\n'.format(_class))

def save_clusters_png(filename, classes, points):
    """Save clusters into a png file.

    Args:
        filename (str): Output filename.
        classes (list): Class of each data point.
        poits(list): List of tuple representing points as (x, y).
    """
    colormap = {
        0: 'black',     5: 'gray',
        1: 'green',     6: 'yellow',
        2: 'blue',      7: 'brown',
        3: 'red',       8: 'magenta',
        4: 'purple',    9: 'cyan'
    }

    for i, c in enumerate(classes):
        i, x, y = points[i]
        plt.plot(x, y, marker='o', ms=2, color=colormap[c])

    plt.savefig(filename, dpi=300)