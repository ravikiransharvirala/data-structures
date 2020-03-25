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
        """This operation adds an item to the stack"""
        self.items.append(item)

    def pop(self):
        """This operation removes an item from the top of the stack""" 
        return self.items.pop()

    def is_empty(self):
        """This operation check if the the stack is empty"""
        return self.items == []

    def peek(self):
        """This operation returns the item that is on top of the stack"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def get_stack(self):
        """This operation returns all the elements in the stack"""
        return self.items