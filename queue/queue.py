#-*- coding: utf-8 -*-
"""
Implementation of data structure queue in python

Queue data structure has four main operations
1. Enqueue -> add store an item to the queue
2. Dequeue -> remove an item from the queue
3. Peek -> get the first element of the 
4. isempty -> check if the queue is empty

"""
class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def is_empty(self):
        return len(self.items) == 0
    def dequeue(self, items):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

