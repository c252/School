import numpy as np
import graph #Jim's graph data structure code
from graph import *

def generate_board(x, y):
    """
    Generates a labeled NxN chess board
    I put it in a function because I didn't want to type it out every time :)
    """
    return np.arange(start = 0, stop = x * y, step = 1).reshape((x,y))

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
    >>> board = generate_board(5,5)
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

def moves_to_edges(pos, available):
    edges = []

    for i in available:
        edges.append((pos, i))
    
    return edges

# def knight_tour(b,x,y):
#     avail = get_moves(b, x, y)
#     edges = moves_to_edges(b[x][y], avail)
#     graph = {}
#     graph = edges_to_graph(graph, edges)

#     for _ in range(b.shape[0] * b.shape[1]):
#         for i in avail:
#             #print(f"Possible moves:{avail} \n")
#             x, y = tuple(map(int, np.where(b == i)))
#             avail = get_moves(b, x, y)
#             edges = moves_to_edges(b[x][y], avail)
#             graph = edges_to_graph(graph, edges)

#     return graph

def knight_tour(b, x, y, j):
    avail = get_moves(b, x, y)
    edges = moves_to_edges(b[x][y], avail)
    graph = {}
    graph = edges_to_graph(graph, edges)

    if j <= b.shape[0] * b.shape[1]:
        for i in avail:
            #print(f"Possible moves:{avail} \n")
            x, y = tuple(map(int, np.where(b == i)))
            avail = get_moves(b, x, y)
            edges = moves_to_edges(b[x][y], avail)
            graph = edges_to_graph(graph, edges)
            knight_tour(b,x,y,(j + 1))

def main():
    startx = 0
    starty = 0
    x = startx
    y = starty

    b = generate_board(5,5) #remember to put in error handeling for boards smaller than 3 and just generally places that have no possible moves
    
    print(f"{b} \n")
    """
    print("Coordinates of moves:")
    for i in avail:
        print(np.where(b == i))
    """

    graph = knight_tour(b, x, y, 0)

    recorder1 = Recorder()
    search(graph, b[startx][starty], "depth", recorder1)
    print(f"Path: {recorder1.replay()}")



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()