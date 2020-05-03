from sys import stdout
from time import sleep


class Stack():
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.pop()
        else:
            return None


class Queue():
    def __init__(self):
        self.storage = []
        self.size = 0

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size:
            self.size -= 1
            return self.storage.pop(0)
        else:
            return None


directions = {
    'n': {
        'invert': 's',
        'name': 'North'
    },
    's': {
        'invert': 'n',
        'name': 'South'
    },
    'e': {
        'invert': 'w',
        'name': 'East'
    },
    'w': {
        'invert': 'e',
        'name': 'West'
    }
}
