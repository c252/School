"""
|Jim Mahoney|

|Modified by Cyrus Burt|

 graph.py

 Playing around with a graph and 
 depth-first vs breadth-first search.

   $ python graph.py 
   graph { /* --- graphviz --- */ 
    a -- b ;
    a -- c ;
    a -- d ;
    b -- e ;
    b -- f ;
    c -- g ;
    c -- h ;
    f -- c ;
    f -- g ;
    h -- d ;
   {rank=same; b c d};
   {rank=same; e f g h};
   }
   
   -- graph node:node --
   {'a': {'b': True, 'c': True, 'd': True},
    'b': {'a': True, 'e': True, 'f': True},
    'c': {'a': True, 'f': True, 'g': True, 'h': True},
    'd': {'a': True, 'h': True},
    'e': {'b': True},
    'f': {'b': True, 'c': True, 'g': True},
    'g': {'c': True, 'f': True},
    'h': {'c': True, 'd': True}}
   
   -- depth-first search --
    -> a -> d -> h -> c -> g -> f -> b -> e
   
   -- breadth-first search --
    -> a -> b -> c -> d -> e -> f -> g -> h
    
Jim Mahoney | cs.marlboro.college | Feb 2019 | MIT License
"""

class Stack:
    """ first in, last out 
        >>> s = Stack()
        >>> s.push(1); s.push(2); s.push(3)
        >>> 1 in s
        True
        >>> (s.pop(), s.pop(), s.pop())
        (3, 2, 1)
        >>> len(s)
        0
    """
    def __init__(self):
        self.values = []
        self.has = {}    # also put values in a dictionary
    def __len__(self):
        return len(self.values)
    def __contains__(self, value):
        # implement the "_ in _" python syntax.
        return value in self.has
    def push(self, value):
        self.values.append(value)
        self.has[value] = True
    def pop(self):
        value = self.values.pop()
        self.has.pop(value)   # remove from dictionary
        return value

class Queue(Stack):
    """ first in, first out 
        >>> q = Queue()
        >>> q.push(1); q.push(2); q.push(3)
        >>> 5 in q
        False
        >>> (q.pop(), q.pop(), q.pop())
        (1, 2, 3)
        >>> len(q)
        0
    """
    def pop(self):
        value = self.values.pop(0)
        self.has.pop(value)
        return value
    
class Recorder:
    """ A callable object (i.e. acts like a function)
        which can store things and replay them.
          >>> record = Recorder()
          >>> record('a')
          >>> record('b')
          >>> record.replay()
          ' -> a -> b'
    """
    def __init__(self):
        self.memory = ""
    def __call__(self, data):
        # (Defines what to do when an instance is treated like a function.)
        self.memory += ' -> ' + str(data)
    def replay(self):
        return self.memory

def edges_to_dot(edges, graph_or_digraph='graph', arrow='--',
                 lined_up=(('b', 'c', 'd'), ('e', 'f', 'g', 'h'))):
    """ Output graphviz .dot representation of graph given its edges. """
    result = '{} {{ /* --- graphviz --- */ \n'.format(graph_or_digraph)
    for (parent, child) in edges:
        result += ' {} {} {} ;\n'.format(parent, arrow, child)
    for same in lined_up:
        result += '{{rank=same; {}}};\n'.format(' '.join(same))
    return result + '}\n'

def edges_to_graph(graph_in, edges):
    """ 
    Modified so that a graph can have edges appended to it
    Return graph adjancency structure i.e. {node: {neighbors}} """
    graph = graph_in
    for (a, b) in edges:
        for (node, neighbor) in ((a, b), (b, a)):
            if not node in graph:
                graph[node] = {}
            graph[node][neighbor] = True
    return graph

def prettyprint(thing):
    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint(thing)
    
def search(graph, start, which, function):
    """ depth-first or breadth-first  search """
    visited = {}               # Nodes which we're done with.
    if which == 'depth':       # Create a fringe of nodes-to-visit ...
        fringe = Stack()           # ... either a stack
    else:
        fringe = Queue()           # ... or a queue.
    fringe.push(start)         # Initialize the search.
    while len(fringe) > 0:     # Search loop:
        node = fringe.pop()                    # Get node to process.
        visited[node] = True                   # Mark it as 'processed'.
        function(node)                         # Do something with it.
        neighbors = sorted(graph[node].keys()) # Get neighbors.
        for candidate in neighbors:            # Add new ones to fringe.
            if not candidate in visited and not candidate in fringe:
                fringe.push(candidate)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
