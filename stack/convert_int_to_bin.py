#-*- coding: utf-8 -*-
"""
Use a stack data structure to convert integer values to binary.

Example:


"""
import timeit
from stack import Stack

def int_to_bin(num):
    stack_bin = Stack()
    while num > 1:
        stack_bin.push(num%2)
        num = int(num/2)
    fbin = str(num)
    while not stack_bin.is_empty():
        fbin = fbin+str(stack_bin.pop())
    return fbin

setup_code = """
from __main__ import int_to_bin
num = 146
"""

print(int_to_bin(146))
print(timeit.timeit(stmt="int_to_bin(num)", setup=setup_code, number=10000))