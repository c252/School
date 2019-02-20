def generate_board(n):
    """
    Generates a labeled NxN chess board
    >>> generate_board(5)
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24]])
    """
    board = np.ones(n**2, dtype=int)

    for i in range(0, n ** 2):
        board[i] = i

    board = board.reshape((n,n))

    return board

def get_moves(x, y):
    moves = []



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()