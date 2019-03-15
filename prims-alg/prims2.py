from minheap import *

A='A';B='B';C='C';D='D';E='E';F='F';G='G';H='H';I='I';J='J';K='K';L='L';M='M'
N='N';O='O';P='P';Q='Q';R='R';S='S';T='T';U='U';V='V';W='W';X='X';Y='Y';Z='Z'

graph_1 = { A : {B:6, D:4, I:9},
            B : {A:6, D:3, E:1, C:3},
            C : {B:3, E:2, F:2},
            D : {A:4, B:3, E:4, G:6},
            E : {B:1, C:2, F:8, H:7, G:6, D:4},
            F : {C:2, E:8, H:11},
            G : {D:6, H:3, J:2, I:2, E:6},
            H : {E:7, F:11, J:4, G:3},
            I : {A:9, G:2, J:1},
            J : {I:1, G:2, H:4},
           }

def add_edge(graph, v0, v1, weight):
    """
    Small helper function to connect 2 nodes in a graph. 
    *destructive function*.
    """
    graph[v0][v1] = weight
    graph[v1][v0] = weight

def edges_to_graph(edges, existing_graph=None):
    """
    converts edges to graphs. It can also add an edge to a graph
    if you use the optional existing_graph arg.
    where an edge is a tuple (Node1, Node2, Weight)
    ie. (A, B, 5)
    This is Jim's edges to graph function modified for weighted graphs
    >>> edges = [(A, B, 4), (A, C, 7), (C, B, 8)]
    >>> edges_to_graph(edges)
    {'A': {'B': 4, 'C': 7}, 'B': {'A': 4, 'C': 8}, 'C': {'A': 7, 'B': 8}}
    """
    if existing_graph:
        graph = existing_graph
    else:
        graph = {}

    for (a, b, w) in edges:
        for (node1, node2) in ((a, b), (b, a)):
            if not node1 in graph:
                graph[node1] = {}
            graph[node1][node2] = w
    return graph
        
def min_edge(node):
    """
    Input a node with connections.
    Returns node with smallest weight.
    Efficiency: O(n)
    """
    minim = list(node.keys())[0] #assume the first connection is shortest
    for i in node:
        if node[i] <= node[minim]:
            minim = i
    return minim

def prims(graph, start):
    min_tree = {}
    edges_queue = MinHeap()
    for i in graph:
        for j in graph[i]:
            edges_queue.insert(tuple([graph[i][j], i, j]))

    for _ in range(len(edges_queue)):
        print(edges_queue.getmin())

if __name__ == "__main__":
    import doctest
    doctest.testmod()