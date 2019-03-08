"""
prims.py
"""

class Node():
    """
    simple node class
    """
    def __init__(self, name, seen=False):
        self.name = name
        self.edges = {}
        #Boolean flag if the node has been seen by the algorithm
        self.seen = seen
    
    def add_edge(self, end_point, weight):
        #This makes it easier to connect nodes, because you don't have to type node.name
        if str(type(end_point)) == "<class '__main__.Node'>":
            end_point = end_point.name
        self.edges[end_point] = weight

    def remove_edge(self, end_point):
        #This function was only for debug purposes
        del self.edges[end_point]

class Graph():
    """
    OO wrapper for an adjacency list graph using dictionaries
    """
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node.edges

    def add_edge(self, v0, v1, weight):
        v0.add_edge(v1, weight)
        v1.add_edge(v0, weight)

if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.add_edge(b, 5)
    a.add_edge(c, 3)
    a.add_edge(d, 6)

    b.add_edge(a, 5)
    c.add_edge(a, 3)
    d.add_edge(a, 6)