class node:#Jim's code
    def __init__(self, value):
        self.value = value
        self.next = None
    def subtree_length(self):
        if self.next == None:
            return 0
        else:
            return 1 + self.next.subtree_length()

class stack():
    def __init__(self):
        self.first = None

    def push(self, value):
        if self.first == None:
            self.first = node(value)
        else:
            
