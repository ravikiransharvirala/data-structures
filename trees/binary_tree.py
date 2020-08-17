#-*- coding: utf-8 -*-
class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def is_empty(self):
        return len(self.items) == 0
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)

class Stack(object):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items) == 0
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root)
        elif traversal_type == "reverselevelorder":
            return self.reverse_levelorder_print(self.root)
        else:
            print("Traversal type {} is not supported.".format(traversal_type))
    
    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
    def levelorder_print(self, start):
        """Print element from each level"""
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek())+ "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    
    def reverse_levelorder_print(self, start):
        """print element from each level in reverse from bottom"""
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()
        traversal = ""

        queue.enqueue(start)
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value)+"-"
        
        return traversal
    
    def height(self, node):
        if node is None:
            return -1
        
        height_left = self.height(node.left)
        height_right = self.height(node.right)

        return 1 + max(height_left, height_right)
    
    def size(self, node):
        if node is None:
            return 0
        
        stack = Stack()
        stack.push(node)
        tree_size = 1

        while len(stack) > 0:
            n = stack.pop()
            tree_size += 1
            
            if n.left:
                stack.push(n.left)
            
            if n.right:
                stack.push(n.right)
        
        return tree_size


    

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.left.left = Node(9)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverselevelorder"))

print(tree.height(tree.root))
print(tree.size(tree.root))