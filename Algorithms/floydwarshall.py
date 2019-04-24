import random
import numpy as np
import matplotlib.pyplot as plt

inf = float("inf")

def floydwarshall(node_num, graph):
    """
    Takes in an adjacency matrix. 
    Returns all the shortest paths,
    from every node to every other node.
    >>> floydwarshall(4, mat_2)
    [[0, 5, 8, 9], [inf, 0, 3, 4], [inf, inf, 0, 1], [inf, inf, inf, 0]]
    """
    sp = graph #I didn't want to function to be destructive
    for i in range(node_num):
        for j in range(node_num):
            for k in range(node_num):
                if sp[i][j] > (sp[i][k] + sp[k][j]):
                    sp[i][j] = sp[i][k] + sp[k][j]
    return sp

def floydwarshall_stepcount(node_num, graph):
    steps = 0
    sp = graph
    steps += 1
    for i in range(node_num):
        steps += 1
        for j in range(node_num):
            steps += 1
            for k in range(node_num):
                steps += 1
                if sp[i][j] > (sp[i][k] + sp[k][j]):
                    sp[i][j] = sp[i][k] + sp[k][j]
    return steps

mat_1 = [
    [0, inf, 6, 3],
    [inf, 0, 2, 7],
    [6, 2, 0, 5],
    [3, 7, 5, 0],
]

mat_2 = [
    [0, 5, inf, 10], 
    [inf, 0, 3, inf], 
    [inf, inf, 0, 1], 
    [inf, inf, inf,0]
]

mat_3 = [
    [0, 6, 2],
    [6, 0, 5],
    [2, 5, 0]
]

def random_graph(n, m):
    inf = float("inf")
    adj_mat = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            x = random.randint(1,4)
            if x == 1:
                adj_mat[i][j] = inf
            else:
                w = random.randint(1,m)
                adj_mat[i][j] = w

    for i in range(n):
        adj_mat[i][i] = 0

    #this looks a little funny but you basically take the matrix, transpose it
    #then you delete the extra so you end up with a matrix that is symetric along
    #main diagonal which is what we want for an adjacency matrix
    adj_mat = adj_mat + adj_mat.T - np.diag(adj_mat.diagonal())

    return adj_mat.tolist()

def main():
    w = 150
    x = np.linspace(0,w)
    y = []
    for i in range(w):
        mat = random_graph(i, 30)
        y.append(floydwarshall_stepcount(i, mat))

    #I am not totally sure why, but my algorithm and the x**3 line
    #don't quite match up, but the aysmptotic behavoir seems the same
    plt.yscale("log")
    plt.plot(y)
    plt.plot(x**3)
    plt.show()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()