from stack_aug172020 import Stack

def int_to_bin(num):
    num = int(num)
    stack = Stack()
    while num > 1:
        stack.push(num%2)
        num = num//2
    bin_string = ""
    while not stack.is_empty():
        bin_string = bin_string+str(stack.pop())
    return bin_string

print(int_to_bin(121))
