import numpy as np
#Jim's graph data structure code
from graph import edges_to_dot, edges_to_graph, Stack

def search(board, n, x, y, path=[]):
    """
    This algorithm is based on the one here http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingKnightsTour.html
    I didn't end up using the graph data structure that is included in graph.py
    but the visualizations are still very helpful in my oppinion
    """
    path.append(board[x][y])
    avail = get_moves(board, x, y)
    if n == board.size - 1:
        print(path)
        exit() #I couldn't figure out a clean way to end the recursion once a path was found
    else:
        for i in avail:
            if i not in path:
                x, y = tuple(map(int, np.where(board == i)))
                search(board, n+1, x, y, path)

        path.pop()

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

def main():
    b = generate_board(6)
    edges = generate_edges(b)
    graph = {}
    graph = edges_to_graph(graph, edges)
    
    print(b)
    search(b, 0, 1, 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()ls