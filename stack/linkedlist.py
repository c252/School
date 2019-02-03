"""
 linkedlist.py

 >>> three = LinkedList([1,2,3])
 >>> three.first.value
 1
 >>> three.last.value
 3
 >>> len(three)
 3

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def subtree_length(self):
        if self.next == None:
            return 0
        else:
            return 1 + self.next.subtree_length()

class LinkedList:
    def __init__(self, values):
        self.first = None
        self.last = None
        for value in values:
            self.push(value)
    def __len__(self):
        # --- the recursive approach ---
        # if self.is_empty():
        #   return 0
        # else:
        #   return 1 + self.first.subtree_length()
        # --- the explicit loop approach ---
        result = 0
        node = self.first
        while node:
            result += 1
            node = node.next
        return result
    def is_empty(self):
        return self.first == None
    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

if __name__ == '__main__':
    import doctest
    doctest.testmod()