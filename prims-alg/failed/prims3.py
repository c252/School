from minheap import *

A='A';B='B';C='C';D='D';E='E';F='F';G='G';H='H';I='I';J='J';K='K';L='L';M='M'
N='N';O='O';P='P';Q='Q';R='R';S='S';T='T';U='U';V='V';W='W';X='X';Y='Y';Z='Z'

"""
prims3.py

I decided to go back to having the nodes and graphs
be OO because the prims2 code was starting to get messy
even before I realized that it wouldn't work
"""
class Node():
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.distance = float("inf")
    
    def addEdge(self, node, weight):
        self.neighbors[node] = weight
    
    def getName(self):
        return self.name

    def delEdge(self, node):
        del self.neighbors[node]

class Graph():
    """
    >>> graph_1 = Graph()
    >>> for i in [A, B, C, D, E, F]:
            graph_1.addNode(i)
    """
    def __init__(self):
        self.nodes = {}

    def addNode(self, new_node):
        self.nodes[new_node] = Node(new_node)

    def addEdge(self, node_0, node_1, weight):
        if node_0 in self.nodes:
            self.addNode(node_0)
        if node_1 in self.nodes:
            self.addNode(node_1)
        self.nodes[node_0].addEdge(self.nodes[node_1], weight) 

    def listNodes(self):
        return self.nodes.keys()           

    def __contains__(self, node):
        return node in self.nodes