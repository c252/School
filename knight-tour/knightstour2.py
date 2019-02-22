import numpy as np
import graph #Jim's graph data structure code
from graph import *

def generate_board(n):
    """
    Generates a labeled NxN chess board
    """
    return np.arange(start = 0, stop = n * n, step = 1).reshape((n, n))

def get_moves(board, x, y):
    """
    ----------------
    |  |2 |  | 3|  |
    ----------------
    |1 |  |  |  | 4|
    ----------------
    |  |  |KN|  |  |
    ----------------
    |8 |  |  |  | 5|
    ----------------
    |  |7 |  | 6|  |
    ----------------
    >>> board = generate_board(5)
    >>> get_moves(board, 0, 0)
    [7, 11]
    >>> get_moves(board, 2, 2)
    [3, 9, 19, 23, 21, 15, 5, 1]
    """
    #The following arrray is the difference between the X,Y of the knight and its 8 possible moves
    moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    available = []

    for i in moves:
        if 0 <= x + i[0] < board.shape[1]:
            if 0 <= y + i[1] < board.shape[0]:
                available.append(board[x + i[0]][y + i[1]])

    return available

def generate_edges(b):
    edges = []

    for i in range(b.shape[0]):
        for j in range(b.shape[1]):
            avail = get_moves(b, i, j)
            for l in avail:
                edges.append((b[i][j], l))
    return edges

def knight_tour(board, x, y, graph):
    return search(graph, board[x][y], "depth")

def main():
    #print(edges_to_dot(generate_edges(generate_board(5)), lined_up=[]))
    b = generate_board(5)
    edges = generate_edges(b)
    graph = {}
    graph = edges_to_graph(graph, edges)
    
    print(b)
    print(knight_tour(b, 3, 3, graph))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()