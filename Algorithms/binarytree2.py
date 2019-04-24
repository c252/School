"""
binarytree.py

CYRUS BURT |JAN 2019|
"""

#I implemented the binary tree a little differently than the 
#assingment asked for, I hope that is okay

class tree():
    def __init__(self,value): #a tree by default has no children nodes
        self.left = None
        self.right = None
        self.value = value

    def pushl(self, value):
        self.left = tree(value)

    def pushr(self, value):
        self.right = tree(value)

    def subtreelen(self):
        # if (self.right == None) and (self.left == None): #I thought this was necessary but it messed the algorithm up
        #     return 0

        if not self.left:
            return 1

        elif not self.right:
            return 1

        else:
            return 2 + self.left.subtreelen() + self.right.subtreelen()

    def __len__(self):
        return 1 + self.subtreelen()

a = tree("a")
a.pushl("b")
a.pushr("c")
a.left.pushl("d")
a.left.pushr("e")
a.right.pushl("f")
a.right.left.pushr("g")
a.right.left.pushl("h")

print(len(a))