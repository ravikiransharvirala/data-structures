#-*- coding: utf-8 -*-
"""Implementing Stack data structure
Using python in-buit data structures. 

The stack data structure has three main operations
Push, Pop, Peek
"""

class Stack(object):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def get_stack(self):
        return self.items

myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
print(myStack.peek())
print(myStack.pop())
print(myStack.get_stack())