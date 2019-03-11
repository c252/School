"""
minheap.py

Cyrus Burt |MAR 2019|

A simple min heap implementation.
I was not satisfied with my previous implementation
so I am rewriting it for this project
"""

class MinHeap():
    def __init__(self, values=1):
        self.heap = [0] * values
        self.size = 0

	def childl(self, i):
		return 2 * i

	def childr(self, i):
		return i // 2

    def prcup(self, i):

	def insert(self, value):
		self.heap.append(value)