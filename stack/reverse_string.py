#-*- coding: utf-8 -*-
"""
Given a string, return rversed version of it using stack

Example:
"Lionel Messi" -> "isseM lenoiL"

"""
from stack import Stack

def reverse_string(string):
    rstr_stack = Stack()
    for c in string:
        rstr_stack.push(c)
    rstr = ""
    while not rstr_stack.is_empty():
        rstr = rstr+rstr_stack.pop()
    return rstr

print(reverse_string("Lionel Messi"))
