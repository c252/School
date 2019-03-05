class Node():
    def __init__(self, name):
        self.name = name
        self.connections = {} #a dictionary of adjacent nodes and their weights