class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("The value is already in the tree")
    
    def find(self, value):
        if self.root:
            is_found = self._find(value, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, value, cur_node):
        if value < cur_node.value and cur_node.left:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right:
            return self._find(value, cur_node.right)
        if value == cur_node.value:
            return True


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(11))