"""
|Jim Mahoney|
 tree.py

 Playing around a bit with a tree structure, 
 including a depth-first recursive search.

 The tree is 

        a
      / | \
     b  c  d
    /|  |\
   e f  g h

 Running this gives (with python 3.5)

    $ python tree.py 
    digraph { /* --- graphviz --- */ 
     a -> b 
     a -> c 
     a -> d 
     b -> e 
     b -> f 
     c -> g 
     c -> h 
    }
    
    -- tree parent:children --
    {'a': {'b': True, 'c': True, 'd': True},
     'b': {'e': True, 'f': True},
     'c': {'g': True, 'h': True}}
    
    -- search order --
     -> a -> b -> e -> f -> c -> g -> h -> d

 Discussion questions :
   
   - What's the difference between this and a graph?

   - Is the treedict below the same as an "adjacency list"?
     (Answer: yes, but only if the corresponding graph is a directed one.)

   - What is 'depth-first' mean here?

   - Are there other ways to search?
     If so, how can you implement them?

   - What is 'pre-order' mean?

   (Hint: check out the docs below on search() ...)

 Implementation notes (i.e. things to look up in the python docs) :

   - __callable__
   - import pprint
    
Jim Mahoney | cs.marlboro.college | Feb 2019 | MIT License
"""

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

def edges_to_dot(edges, graph_or_digraph='digraph', arrow='->'):
    """ Output graphviz .dot representation of digraph given its edges. """
    result = '{} {{ /* --- graphviz --- */ \n'.format(graph_or_digraph)
    for (parent, child) in edges:
        result += ' {} {} {}; \n'.format(parent, arrow, child)
    return result + '}\n'

def edges_to_treedict(edges):
    """ Return treedict data structure i.e. {parent: {child:True}} """
    tree = {}
    for (parent, child) in edges:
        if not parent in tree:
            tree[parent] = {}
        tree[parent][child] = True
    return tree

def prettyprint(thing):
    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint(thing)
    
def search(tree, node, function):
    """ a pre-order depth-first recursive search. """
    # (Phew! That's a lot of buzz words. 
    #  See https://en.wikipedia.org/wiki/Tree_traversal .)
    function(node)                     # Apply function to this node.
    kids = tree.get(node, {})          # Get kids (or empty dict if none)
    for child in sorted(kids.keys()):  # Repeat search on kids in alpha order
        search(tree, child, function)

def main():
    """ Playing around with a tree. """

    # Define the tree with (parent,child) tuples.
    edges = [ ('a', 'b'), ('a', 'c'), ('a', 'd'),
              ('b', 'e'), ('b', 'f'),
              ('c', 'g'), ('c', 'h') ]

    # Show a graphviz representation.
    print(edges_to_dot(edges))

    # Convert to a dictionary of parent nodes and their children.
    tree = edges_to_treedict(edges)
    print('-- tree parent:children --')
    prettyprint(tree)
    print()

    # Do a recursive search starting at node 'a',
    # and show the traverseral order.
    print('-- search order --')
    record = Recorder()
    search(tree, 'a', record)
    print(record.replay())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()