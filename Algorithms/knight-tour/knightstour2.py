import numpy as np
#Jim's graph data structure code
from graph import edges_to_dot, edges_to_graph, Stack

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
    #Get the locations of all the offsets and then add them to available if they exist
    for i in moves:
        if 0 <= x + i[0] < board.shape[1]:
            if 0 <= y + i[1] < board.shape[0]:
                available.append(board[x + i[0]][y + i[1]])

    return available

def generate_edges(b):
    """
    This is generating every edge twice because I thought that was how the graph in Jim's code worked
    However this is not the case and the graph is just twice as big as it needs to be
    """
    edges = []
    for i in range(b.shape[0]):
        for j in range(b.shape[1]):
            avail = get_moves(b, i, j)
            for l in avail:
                edges.append((b[i][j], l))
    return edges

def wassenndorf(board, x, y):
    """
    This orders the available children nodes by the number of children they have in descending order
    It's pretty amazing how much this speeds up computation
    """
    avail = get_moves(board, x, y)
    return sorted(avail, key = lambda i: len(get_moves(board, tuple(map(int, np.where(board == i)))[0], tuple(map(int, np.where(board == i)))[1])))

def tour(board, n, x, y, path=[]):
    """
    I didn't end up using the graph data structure that is included in graph.py
    but the visualizations are still very helpful in my oppinion
    """
    path.append(board[x][y])
    avail = wassenndorf(board, x, y)
    if n == board.size - 1:       #If n is the size of the board, all the squares have been used (the -1 is because N is zero indexed)  
        print(path)               #If there is no tour the algorithm prints nothing
        exit()                    #Cleanest way I could think of to completly exit the recursion, If this was removed it would print all of the possible knights paths
    else:
        for i in avail:
            if i not in path:
                x, y = tuple(map(int, np.where(board == i))) #get the x,y coords of I
                tour(board, n+1, x, y, path)                 #recursively call the algorithm on the children

        path.pop()

def main():
    b = generate_board(8)
    edges = generate_edges(b)
    graph = {}
    print(b)
    tour(b, 0, 2, 2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()