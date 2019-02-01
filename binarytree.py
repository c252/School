"""
binarytree.py
>>> x1 = node(4)
>>> x2 = node(6)
>>> x3 = node(9)
>>> y1 = node(9)
>>> y2 = node(32)
>>> y3 = node(12)

>>> x3.left = x1
>>> x3.right = x2
>>> y3.left = y1
>>> y3.right = y2
>>> a = node(324)
>>> b = node(56)
>>> a.left = x3
>>> a.right = y3
>>> b.right = a
>>> b.left = a
>>> c = node(4)
>>> c.left = b
>>> c.right = a
>>> c.subtreelen()
11
"""

class node(object):
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def subtreelen(self):
        if (not self.right) and (not self.left):
            return 0
        if not self.left:
            return 1
        if not self.right:
            return 1
        else:
            return 1 + self.left.subtreelen() + self.right.subtreelen()

class tree(object):
    def __init__(self, values):
        self.last == None
        for value in values:
            self.push(value)

    def push(self, value):
        newNode = node(value)
        if self.last.left != node:
            self.last.left = newNode
        if self.last.right != node:
            self.last.right = newNode
    
        self.last = newNode


if __name__ == '__main__':
    import doctest
    doctest.testmod()