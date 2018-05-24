import matplotlib.pyplot as plt

from utils.graph import euclidean


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

def save_mst_csv(filename, edges):
    """Save MST into a csv file.

    Args:
        filename (str): Output filename.
        edges (list): List of tuple representing edges as (src, dst, weight).
    """
    with open(filename, 'w') as f:
        f.write('source,destination,weight\n')
        for src, dst, weight in edges:
            f.write('{},{},{}\n'.format(src, dst, weight))

def save_mst_png(filename, edges, points):
    """Save MST into a png file.

    Args:
        filename (str): Output filename.
        edges (list): List of tuple representing edges as (src, dst, weight).
        points (list): List of tuple representing points as (x, y).
    """
    for src, dst, _ in edges:
        p, q = [points[src][1], points[dst][1]], [points[src][2], points[dst][2]]
        plt.plot(p, q, marker='o', ms=3, mfc='red', mec='red', color='black')

    plt.savefig(filename, dpi=300)

def save_clusters_csv(filename, classes):
    """Save clusters into a csv file.

    Args:
        filename (str): Output filename.
        classes (list): Class of each data point.
    """
    with open(filename, 'w') as f:
        f.write('class_id\n')
        for _class in classes:
            f.write('{}\n'.format(_class))

def save_clusters_png(filename, classes, points):
    """Save clusters into a png file.

    Args:
        filename (str): Output filename.
        classes (list): Class of each data point.
        points (list): List of tuple representing points as (x, y).
    """
    colormap = {
        0: 'black',    5: 'red',
        1: 'magenta',  6: 'blue',
        2: 'green',    7: 'yellow',
        3: 'orange',   8: 'purple',
        4: 'gray',     9: 'cyan'
    }

    for i, c in enumerate(classes):
        i, x, y = points[i]
        plt.plot(x, y, marker='o', ms=2, color=colormap[c])

    plt.savefig(filename, dpi=300)
