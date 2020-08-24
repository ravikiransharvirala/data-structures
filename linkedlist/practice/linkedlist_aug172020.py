#-*- coding: utf-8 -*-
"""
Singly Linked List
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def display(self):
        if self.head:
            current = self.head
            while current:
                print(current.value)
                current = current.next
        else:
            print("There are no elements in the list")
    
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def search(self, position):
        if self.head:
            if position == 1:
                return self.head.value
            current = self.head
            cur_pos = 1
            while current.next:
                cur_pos += 1
                current = current.next
                if position == cur_pos:
                    return current.value
        else:
            print("There are no elements in the linked list")
            return None
    
    def insert(self, new_value, position):
        new_node = Node(new_value)
        if self.head:
            if position == 1:
                new_node.next = self.head
                self.head = new_node
                pass
            cur_pos = 1
            current = self.head
            while current:
                cur_pos += 1
                if position == cur_pos:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
        else:
            return None
    
    def delete(self, del_val):
        if self.head:
            current = self.head
            previous = None
            while current.next and current.value != del_val:
                previous = current
                current = current.next
            if current.value == del_val:
                if previous:
                    previous.next = current.next
                else:
                    self.head = self.head.next
        else:
            return None
    
    def len_iterative(self):
        if self.head:
            current = self.head
            length = 0
            while current:
                current = current.next
                length += 1
            return length
        else:
            return 0
    
    def len_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.value != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.value != key_2:
            prev_2 = curr_2
            curr_2 =curr_2.next
        
        if not curr_1 or not curr_2:
            return 
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    
test_ll = LinkedList()
test_ll.append("A")
test_ll.append("B")
test_ll.append("C")
test_ll.append("D")
test_ll.insert("Z", 1)
test_ll.display()
test_ll.swap_nodes("A", "C")
print("++++++++++++++++++++++++++")
test_ll.display()

print(test_ll.len_iterative())
print(test_ll.len_recursive(test_ll.head))