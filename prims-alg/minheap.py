"""
minheap.py

Cyrus Burt |MAR 2019|

A simple min heap implementation.
I was not satisfied with my previous implementation
so I am rewriting it for this project
"""

class MinHeap():
    def __init__(self, values):
        self.values = values

    def prcup(self):
        