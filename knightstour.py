import numpy as np
import graph #Jim's graph data structure code

"""
I think I may have gone a little overboard with the chess board generation
if it's too slow I will try to simplify it
"""

def generate_board(x, y):
    """
    Generates a labeled NxN chess board
    >>> generate_board(5, 5)
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24]])
    """
    board = np.ones(x * y, dtype=int)

    for i in range(0, x * y):
        board[i] = i

    board = board.reshape((x,y))

    return board

def get_moves(board, x, y):
    """
    ----------------
    |  |2 |  |3 |  |
    ----------------
    |1 |  |  |  |4 |
    ----------------
    |  |  |K |  |  |
    ----------------
    |8 |  |  |  |5 |
    ----------------
    |  |7 |  |6 |  |
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
        if 0 <= x + i[0] <= board.shape[1] - 1:
            if 0 <= y + i[1] <= board.shape[0] - 1:
                available.append(board[x + i[0]][y + i[1]])

    return available



def main():
    print("hi")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()