import numpy as np
#Jim's graph data structure code
from graph import edges_to_dot, edges_to_graph, Stack, Queue

def search(graph, n, start, path=[]):
    """ depth-first or breadth-first  search """
    visited = {}          # Nodes which we're done with.
    fringe = Stack()           # Create a fringe of nodes-to-visit ...
    fringe.push(start)         # Initialize the search.
    while len(fringe) > 0:     # Search loop:
        node = fringe.pop()                    # Get node to process.
        visited[node] = True                   # Mark it as 'processed'.
        neighbors = sorted(graph[node].keys()) # Get neighbors.

        for i in neighbors:
            if i in visited:
                neighbors.remove(i)

        for candidate in neighbors:
            if not candidate in visited and not candidate in fringe:
                fringe.push(candidate)
    
    return path        

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
    return search(graph, 0, board[x][y])


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

    # for i in avail:
    #     x1, y1 = tuple(map(int, np.where(board == i)))
    #     path = search(graph, board[x1][y1], "depth")
    #     print(f"{path}\n")

    # def search(board, graph, n, x, y,path = [], visited = []):
#     path.append(board[x][y])
#     finished = False
#     counter = 0
#     if n <= len(board) ** 2:         #see if every square was visited
#         avail = get_moves(board, x, y)
#         while counter < len(avail) and not finished:
#             if avail[counter] not in visited:
#                 visited.append(avail[counter])
#                 path.append(avail[counter])
#                 finished = search(board, graph, n+1, x, y, path, visited)
#             counter += 1
#         if not finished:
#             visited.remove(path[-1])
#             path.pop()
#     else:
#         finished = True

#     return path