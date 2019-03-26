Floyd-Warshall Algorithm
========================

The Floyd-Warshall algorithm is a very interesting algorithm
that calculates the shortest path from one node to another
in a graph, there are a few other algorithms that do this like:
Dijkstra's, A-start, Bellman-Ford, etc. The cool thing about Floyd
-Warshall is that it generates the shortest path from every node to
every other node.

In this algorithm, it is cleanest to implement our graphs using
an adjacency matrix. An adjacency matrix works like this:
Say you have a simple graph like this
                1
             6 / \ 5 
              0 - 2
                2

In an adjancey matrix it would be represented like this:
[
    [0,6,2]
    [6,0,5]
    [2,5,0]
]

This way we can find the weight of edge of connection node 1 --- node 2
by looking at the adjacency matrix with the index of either adj[1][2]
or adj[2][1]. The main diagonal is all zeros, because the nodes can't be
connected to themselves with this algorithm.

The Floyd-Warshall algorithm is going to go through this adjacency matrix
and find the shortest paths for each node, it will return a list that looks
like this: [[0, 6, 2], [6, 0, 5], [2, 5, 0]]
The way you would read this, is by looking at the row of the node you
are curious about (In this case I will choose 1), and then the nth column in 
that row will contain the optimal distance to node n. So the optimal distance
in our graph from 0 -> 1 is a distance of 6 (which is pretty easy to see in this
simple example).

Lets see how it works!
The main part of the algorithm is this in pseudocode:
    for i in 0 to N
        for j in 0 to N
            for k in 0 to N
                if matrix[i][j] < matrix[i][k] + matrix[k][j]
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

The first to for loops make sense because we want to calculate the optimal
distance for every single node (every x and y or i and j position of the matrix).
The next three lines took me a while to understand. 

One of the basic ideas with these few lines is that we assume the optimal distance
from point A to point B is matrix[A][B] (Which could be inifity in which case there
is no direct connection), then we find a node C that is connected to A and say "Is this
node C connected to B. If the answer is yes, and the weight of A->C + C-> B is less than
the current best, set the current best to that!" In this pseudo code, the node C is k.
However, C isn't necessarily 1 node it could in theory be every single node in the graph! Because, we are constantly updataing weight of matrix[A][B] throughout the algorithm which
means this might already include the weight of another node. Because of this, the algorithm
checks all of the connections from A to B to get the smallest one. Even though this is done
with three for loops, thinking of it as a recursion problem really helped me to figure it out.

ASCII PICTURE:
        2   
      /  \
     /    \
    1 ---- 3
Is it smaller to go from 1 -> 3 or 1->2->3?


Clearly the big O of Floyd-Warshall is O(N^3) where N is the number of nodes. It is cubed
because there are 3 for loops that go from 1 to N.