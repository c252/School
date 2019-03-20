"""
minheap.py

Cyrus Burt |MAR 2019|

A simple min heap implementation.
I was not satisfied with my previous implementation
so I am rewriting it for this project
This is based on Jim's code for min heap
as well as the article I linked on InteractivePython
"""
class MinHeap():
    """
    A minimum priority queue
    >>> heap = MinHeap()
    >>> heap.heapify([1,5,3,9,12,-5,-2,4])
    >>> heap.heap
    [0, -5, 4, -2, 5, 12, 3, 1, 9]
    >>> heap.pop()
    -5
    >>> heap.heap
    [0, -2, 4, 1, 5, 12, 3, 9]
    """
    def __init__(self):
        #multiplying by 0 so a small buffer is needed
        self.heap = [0]
        self.size = 0
        
    def __len__(self):
        return self.size

    def childl(self, i):
        """
        Returns the left child in minimum heap
        """
        return 2 * i

    def childr(self, i):
        """
        Returns the right child in minimum heap
        """
        return 2 * i + 1

    def parent(self, i):
        """
        Returns the parent in minimum heap
        """
        return i // 2

    def prcup(self, i):
        while self.parent(i) > 0: #Is i's parent the root node?
            if self.heap[i] < self.heap[self.parent(i)]: #is i < or > than its parent?
                self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i) #Now i and i's parent have swapped, continue algorithm until i's parent is < than i

    def smallest_child(self, i):
        if self.childr(i) > self.size:
            return self.childl(i)
        elif self.heap[self.childr(i)] < self.heap[self.childl(i)]:
            return self.childr(i)
        else:
            return self.childl(i)

    def prcdown(self, i):
        while self.childl(i) <= self.size:
            smallest = self.smallest_child(i)
            if self.heap[i] > self.heap[smallest]:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def push(self, value):
    	self.heap.append(value)
    	self.size += 1
    	self.prcup(self.size)

    def pop(self):
        if self.size == 1:
            return None
        result = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.prcdown(1)
        return result

    def heapify(self, values):
        self.size = len(values)
        self.heap = [0] + values
        i = self.size // 2
        while i > 0:
            self.prcdown(i)
            i -= 1

    def decrease_key(self, name, value):
        """
        Find a node and decrease its value
        a node is a tuple like this: (Weight, Node_0, Node_1)
        """
        found = False #have we found the node we are looking for yet?
        key = 0
        for i in range(self.size + 1):
            print(self.heap[i])
            # if found == True:
            #     break
            # if self.heap[i][1] == name[0] and self.heap[i][2] == name[1]:
            #     found = True
            #     key = i
            # else:
            #     i += 1
        
        if key > 0:
            self.heap[key][0] = value
            self.prcup(key)

if __name__ == "__main__":
    import doctest
    doctest.testmod()