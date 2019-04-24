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
    
graph_2 = { A: {B:5, C:2, D:1},
            B: {A:5, C:1},
            C: {A:2, B:1, D:2},
            D: {A:1, C:2}}

edges_1 = [(6, A, B), (4, A, C), (4, B, D), (7, C, B), (9, C, D)]

def add_edge(graph, edge):
    """
    Small helper function to connect 2 nodes in a graph. 
    *destructive function*.
    """
    v0 = edge[1]
    v1 = edge[2]
    weight = edge[0]
    if not v0 in graph:
        graph[v0] = {}
    if not v1 in graph:
        graph[v1] = {}
    graph[v0][v1] = weight
    graph[v1][v0] = weight

def edges_to_dot(edges, graph_or_digraph='digraph', arrow='->'):
    """ *Jim's code* Output graphviz .dot representation of digraph given its edges. """
    result = '{} {{ /* --- graphviz --- */ \n'.format(graph_or_digraph)
    for (parent, child) in edges:
        result += ' {} {} {}; \n'.format(parent, arrow, child)
    return result + '}\n'

def edges_to_graph(edges, existing_graph=None):
    """
    converts edges to graphs. It can also add an edge to a graph
    if you use the optional existing_graph arg.
    where an edge is a tuple (Weight, Node_0, Node_1,)
    ie. (5, A, B)
    This is *Jim's* edges to graph function modified for weighted graphs
    >>> edges = [(4, A, B), (7, A, C), (8, C, B)]
    >>> edges_to_graph(edges)
    {'A': {'B': 4, 'C': 7}, 'B': {'A': 4, 'C': 8}, 'C': {'A': 7, 'B': 8}}
    """
    if existing_graph:
        graph = existing_graph
    else:
        graph = {}

    for (w, a, b) in edges:
        for (node_0, node_1) in ((a, b), (b, a)):
            if not node_0 in graph:
                graph[node_0] = {}
            graph[node_0][node_1] = w
    return graph

def min_edge(queue):
    """
    Input a node with connections.
    Returns node with smallest weight.
    """
    minim = queue[0]
    for i in queue:
        if i[0] < minim[0]:
            minim = i
    #ToDo Rewrite remove as to show it's proper big O
    queue.remove(minim)
    return minim

def prims(graph, start):
    inf = float("inf")#the initial distances of the edges is set to infinity in prim's algorithm
    min_tree = {}
    #edges_queue = MinHeap()
    #a bit of an awkward way to make sure we don't up using the same edge twice like (5, A, B) and (5, B, A)
    seen = {}
    edges = []
    for i in graph:
        seen[i] = True
        for j in graph[i]:
            if j not in seen: 
                edges.append((inf, i , j))
    
    for i in range(len(edges)):
        if start in edges[i][1:]:
            edges[i] = tuple([graph[edges[i][1]][edges[i][2]], edges[i][1], edges[i][2]])
    
    add_edge(min_tree, min_edge(edges))

    for current_node in list(min_tree.keys()):
        for i in range(len(edges)):
            if current_node in edges[i][1:]:
                edges[i] = tuple([graph[edges[i][1]][edges[i][2]], edges[i][1], edges[i][2]])

        #cycle detection
        candidate = min(edges)
        if candidate[1] in min_tree.keys() != candidate[0] in min_tree.keys():
            add_edge(min_tree, candidate)
        else:
            edges.remove(candidate)

    print(f"Queue: {edges}, LENGTH:{len(edges)} \n \n Min Tree: {min_tree}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# if min(edges)[1] in min_tree.keys() or min(edges)[2] in min_tree.keys():
#     add_edge(min_tree, min_edge(edges))
# else:
#     edges.remove(min(edges))