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
    min_tree = []
    for i in graph:
        candidates = list(graph[i].keys()) #get the possible nodes to add to the tree as a list
        candidates = sorted(candidates, key = lambda x: graph[i][x])
        print(candidates)
        # for v in graph[i]:
        #     print(f"NODE: {i} {min_edge(graph[i])}")
        #     print(v)
        #     min_tree.append(min_edge(graph[i]))