"""
stack.py
an implementation of a stack using linked lists
"""
class node:#Jim's code slightly modified
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

    def empty(self):
        return self.first == None

    def push(self, value):
        newnode = node(value)
        if self.first == None:
            self.first = newnode
        else:
            newnode.next = self.first
            self.first = newnode

    def pop(self):
        if self.empty() == True:
            return "empty"

        else:
            result = self.first.value
            self.first = self.first.next
            return result

    def peek(self):
        return self.first.value

    def __len__(self):
        return 1 + self.first.subtree_length()
            

def parens_balence(string):

    s = stack()

    p = 1

    for i in list(string):
        if i == "(":
            s.push("(")

        if i == ")":
            s.pop()

        if s.empty():
            p -= 1

    if p != 0:
        return False
    else:
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()