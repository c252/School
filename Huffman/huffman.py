"""
 huffman.py

 Generate a huffman code from symbol probabilities.
 
 tested with python 3.5.2
 
 Jim M | Jan 2017 | MIT License

 Modified By:
 Cyrus B | Apr 2019

 tested with python 3.7.1
 #changed some of the code to use some newer python features
"""

import sys
sys.setrecursionlimit(5000)

class PriorityQueue(object):
    """ A min priority queue is a data structure which can
          * push : add items (push), 
          * pop  : remove the smallest, or
          * peek : return the smallest.
        >>> pq = PriorityQueue([5, 3, 10, 7])
        >>> (pq.pop(), pq.pop())
        (3, 5)
        >>> pq.push(9)
        >>> (pq.pop(), pq.pop())
        (7, 9)
    """
    # This implementation is simple though not particularly
    # efficient. The list keeps the smallest element first, the rest
    # unordered.  When the smallest is popped, an O(n) pass through
    # the list finds the new smallest and makes it the rist. Pushing
    # is O(1), since the new item is copmared to the first to see
    # which is smaller. An implementation with a heap would be faster
    # with log(n) effienciency, but I didn't bother with that here.
    
    def __init__(self, items=[], sortkey=lambda x:x):
        self.items = list(items) # store a shallow copy
        self.sortkey = sortkey   # how to get a sortable number from an item
        self._min_to_front()
          
    def _less_than(self, item1, item2):
        return self.sortkey(item1) < self.sortkey(item2)
    
    def _min_to_front(self):
        """ move smallest entry in self.items to its front """
        for i in range(len(self.items)):
            if self._less_than(self.items[i], self.items[0]):
                (self.items[i], self.items[0]) = \
                (self.items[0], self.items[i])                
                
    def push(self, item):
        self.items.append(item)
        if self._less_than(self.items[-1], self.items[0]):
            (self.items[-1], self.items[0]) = (self.items[0], self.items[-1])
            
    def peek(self):
        return self.items[0]
    
    def pop(self):
        item = self.items.pop(0)
        self._min_to_front()
        return item

class BinaryTree(object):
    """ A node in a binary tree """
    # or equivalently the root of a binary subtree
    
    def __init__(self, name='', data=0, 
                 parent=None, left=None, right=None):
        self.name = name if name != '' else str(data)
        self.data = data
        self.parent = parent
        self.set_children(left, right)
        
    def set_children(self, left, right):
        self.left = left
        self.right = right
        for child in (left, right):
            if child != None:
                child.parent = self

class Huffman(PriorityQueue):
    """ Create a Huffman code from a dict of symbols and probabilities.
        >>> h = Huffman({'00': 0.6, '01': 0.2, '10': 0.1, '11': 0.1})
        >>> sorted( h.huffman_code.items() ) # [ (symbol, huffman_code), ...]
        [('00', '1'), ('01', '00'), ('10', '010'), ('11', '011')]
        >>> h.mean_code_length()  # Symbols '00' etc are length 2.
        1.6
        >>> h.max_code_length()   # Longest of huffman codes.
        3
        >>> print(h.code_table()[:-1])    # Omit last newline
        0x3030 1
        0x3031 00
        0x3130 010
        0x3131 011

        (Here 0x3030 is '00' in ascii, namely one of the original symbols.
         As the most probable, it gets the shortest huffman code, namely 1.)
    """

    def __init__(self, symbol_probabilities):
        self.probabilities = symbol_probabilities
        self.symbols = sorted(self.probabilities.keys())
        self.huffman_tree = None   # root of huffman binary tree
        self.huffman_code = {}     # {symbol:code} dictionary
        PriorityQueue.__init__(self, sortkey = lambda x: x.data)
        for (symbol, probability) in sorted(self.probabilities.items()):
            self.push(BinaryTree(name=symbol, data=probability))
        self.leaves = self.items[:] # save a copy of list of terminal nodes
        self._build_huffman_tree()
        self._build_huffman_code()
        
    def _build_huffman_tree(self):
        """ Build the huffman tree and store it in self.huffman_tree """
        # The idea is to repeatedly create a new node in the tree
        # whose probability is the sum of the two smallest which 
        # haven't yet been combined. Here this is accomplished with
        # two data structures: a PriorityQueue to keep track of which
        # probabilities still need to be looked at, and which is 
        # the smallest, and a BinaryTree collection.
        while len(self.items) > 1:
            item1 = self.pop()
            item2 = self.pop()
            data = item1.data + item2.data # probability
            self.huffman_tree = BinaryTree(name='********', data=data, 
                                           left=item1, right=item2)
            self.push(self.huffman_tree)
            
    def _build_huffman_code(self, node=None, code=''):
        """ Build a dictionary of {symbol:codeword} in self.huffman_code """
        if node == None:
            node = self.huffman_tree
        if node.name == '********':  # intermediate node ?
            self._build_huffman_code(node.left, code + '0')
            self._build_huffman_code(node.right, code + '1')
        else:                    # terminal node, i.e. an original symbol
            self.huffman_code[node.name] = code
            
    def mean_code_length(self):
        mean = 0.0
        for sym in self.symbols:
            mean += self.probabilities[sym] * len(self.huffman_code[sym])
        return mean
    
    def max_code_length(self):
        return max([len(self.huffman_code[sym]) for sym in self.symbols])
    
    def min_code_length(self):
        return min([len(self.huffman_code[sym]) for sym in self.symbols])
    
    def code_table(self):
        result = ''
        for sym in sorted(self.symbols):
            hex = '0x' + ''.join("{:02x}".format(ord(c)) for c in sym)
            result += f"{hex}, {chr(int(hex, 16))}: {self.huffman_code[sym]}"
        return result
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()