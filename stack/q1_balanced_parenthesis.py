#-*- coding: utf-8 -*-
"""Use a stack to check whether or not a string has balanced
parenthesis

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

from stack import Stack

def balanced_parenthesis(paren_string):
    p_dict = {")" : "(", "}" : "{", "]" : "["}
    s_paren = Stack()
    for p in paren_string:
        if p in p_dict.values():
            s_paren.push(p)
        elif p in p_dict.keys():
            if s_paren.is_empty() or s_paren.pop() != p_dict[p]:
                return False
        else:
            return False
    return s_paren.is_empty()

print(balanced_parenthesis("{[]}"))