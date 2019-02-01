"""
binarytree.py
>>> x1 = node(None,None,4)
>>> x2 = node(None,None,6)
>>> x3 = node(x1,x2,9)
>>> x3.subtreelen()
3
"""

class node(object):
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def subtreelen(self):
        if self.left:
            return 1
        if self.right:
            return 1
        else:
            return 2 + self.left.subtreelen() + self.right.subtreelen()

class tree(object):
    def __init__(self, values):
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()