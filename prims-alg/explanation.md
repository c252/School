Problems
======
Hi Jim, I was unable to implement the algorithm, I tried for many days, rewrote it many times, 
changed my data structures. I just couldn't get it to work. I am really sorry for not being able to complete the project, 
and not asking for help when I really should have.


I still would really appreciate some help though, because I do genuinely want to get it working.

Prim's algorithm explanation
=====
Prim's algorithms is an graph algorithm that generates a Minimum Spanning Tree.

When you have a graph (a number of nodes that are connected), the graph will always
have a tree (a connected acyclic graph) that can be embedded inside of it. So if 
N is the set of all nodes in a graph and E is the set of edges, then the embedded tree
will have a set of nodes M such that M = N, and a set of edges H where H ⊂ E such that
none of the edges chosen will cause a cycle in the embedded tree. (tree.png is an example
of what I am talking about). So the tree contains every node in the graph without creating any
cycles (so every node has exactly one path to connect to another node).

In a weighted graph, the spanning trees will also have weights. The total weight of the
spanning tree would be defined as \[ \sum_{e}^{T} weight(e) \] or the weight of all the 
edges added together. The MST of a graph is an embedded tree that has the smallest total weight.

Let's see how Prim's algorithm does this:

In Prim's algorithm we start with an arbitrary node (because the MST is going to contain
every node, it doesn't matter where we start)

Now we take all of the edges in the graph we are working on and put them in a container
the data structure we use here will change the big O of the algorithm since finding the
smallest edge is the core operation of the whole algorithm. If we use a python list (array)
it will be O(n) to add all the elements to the list (I think) and it will be a O(n) operation to find the smallest edge, if we use a binary min-heap it will
be a O(log(n)) to build  the heap and then a O(1) to get the minimum edge.

Right now our pseudo-code for Prim's algorithm would look like this:
    
    while edges_queue not empty:
        find smallest safe* edge (a,b)
        add (a,b) to MST

*safe meaning: does not create a cycle, and the MST remains connected 

adding an edge to the MST is very easy, if it is an adjacency list we just say that 
    MST[B] = graph[A][B]
    MST[A] = graph[A][B]

The tricky part is finding a safe edge. We need to make sure that a cycle is not created and 
the tree remains connected so we will check to make sure that only 1 node in the candidate
minimum edge is in the MST.

However we want to make absolutely sure that our candidate edge is either going to immediatley
be placed in the MST or is not needed in which case we just delete it. This is why we start
with all the edges having a weight of infinity except the ones that are connected to nodes
already in the MST (which at the beginning is only the starting node). So whenever the MST 
increases in size we will run a decreasekey operation on the heap to get the true values
whatever edges are immediate candidates. So in my example pictures we start with node A, then
we go through the heap and decrease the values of the edges connected to A: so (inf, A, D) -> (2, A, D), (inf, A, B) -> (3, A, B). With the decreasekey operation the values are always percolated back up so the heap state is maintained and the pop operation will give us the edge to add to the MST (which in this case is (A, D)).

Using all this information we case reason that the big O of Prim's algorithm with a min heap
will be O(log(N)) to heapify the nodes then we are going to go through every node O(N) and decrease it's key O(E). This gives us O(E*log(N) + 2N), and since big O is only the asymptotic 
efficiency it's actually O(E*log(N) + N).