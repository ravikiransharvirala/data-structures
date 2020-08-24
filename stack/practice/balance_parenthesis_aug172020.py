from stack_aug172020 import Stack

def balanced_parenthesis(paren_string):
    stack = Stack()
    paren_dict = {')':'(', ']':'[', '}':'{'}
    for paren in paren_string:
        if paren in paren_dict.values():
            stack.push(paren)
        elif paren in paren_dict.keys():
            if stack.is_empty() or stack.pop() != paren_dict[paren]:
                return False
        else:
            return False
    return stack.is_empty()

print(balanced_parenthesis("[][]"))