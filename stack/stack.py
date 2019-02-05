"""
stack.py
an implementation of a stack using linked lists

>>> check_parens("((()))()")
True
>>> check_parens("(((((((()(()")
False
"""
class node:#Node class for the linked list
    def __init__(self, value):
        self.value = value
        self.next = None
    def subtree_length(self):
        if self.next == None:
            return 0
        else:
            return 1 + self.next.subtree_length()

class stack(): #stack implementation with linked list
    def __init__(self):
        self.first = None

    def empty(self):
        return self.first == None

    def push(self, value): #some simple logic to add new nodes and link them
        newnode = node(value)
        if self.first == None:
            self.first = newnode
        else:
            newnode.next = self.first
            self.first = newnode

    def pop(self):
        if self.empty() == True: #returns None if a pop from an empty stack is attempted
            print("empty")
            return None

        else:
            result = self.first.value
            self.first = self.first.next
            return result

    def peek(self):
        return self.first.value

    def __len__(self):
        return 1 + self.first.subtree_length()



#This is the code from the RSI website, but modified to use my 
# linked list based stack implementation
##################################################
def check_parens(symbolString):
    s = stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.empty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.empty():
        return True
    else:
        return False
#################################################


if __name__ == "__main__":
    import doctest
    doctest.testmod()