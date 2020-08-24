#-*- coding: utf-8 -*-

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
    
    def append(self, new_element):
        new_node = Node(new_element)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def insert_at_begin(self, new_element):
        new_node = Node(new_element)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
    
    def insert_at_end(self, new_element):
        new_node = Node(new_element)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def insert_by_position(self, new_element, position):
        new_node = Node(new_element)
        if self.head:
            if position == 1:
                new_node.next = self.head
                self.head = new_node
            current = self.head
            cur_pos = 1
            while current:
                cur_pos += 1
                if cur_pos == position:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
        else:
            print("There are no elements in the Linked List")
    
    def insert_after_value(self, new_element, value):
        new_node = Node(new_element)
        if self.head:
            current = self.head
            while current and current.value != value:
                current = current.next
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
        else:
            print("There are no elements in the Linked List")


LL = LinkedList()
LL.append('a')
LL.append('b')
LL.append('c')
##LL.insert_at_begin()
LL.display()