#-*- coding: utf-8 -*-
"""
Implemention of linked list data structure in python.

Linked List data structure has four main operations
Append -> add an item to the existing LL
Search -> get an item from a spot in the LL 
Insert -> insert an item in the LL based on the certain position
Delete -> delete an item from the LL

"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = None
    
    def append(self, new_element):
        new_node = Node(new_element)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def display(self):
        if self.head:
            current = self.head
            while current:
                print(current.value)
                current = current.next
        else:
            print("There is no data in the linkedlist ")
    
    def search(self, position):
        if self.head:
            current = self.head
            if position == 1:
                return current.value
            cur_pos = 1
            while current.next:
                current = current.next
                cur_pos += 1
                if cur_pos == position:
                    return current.value
            print("There is no data at position {} and the linked list has only {} values".format(position, cur_pos))
        else:
            print("There are no elements in the LinkedList")
            return None
    def insert(self, position, new_element):
        new_node = Node(new_element)
        if self.head:
            if position == 1:
                new_node.next = self.head
                self.head = new_node
            cur_pos = 1
            current = self.head
            while current.next:
                cur_pos += 1
                if cur_pos == position:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
        else:
            return None
    
    def delete(self, del_val):
        if self.head:
            current = self.head
            previous = None
            while current.next and current.value != del_val:
                previous =  current
                current = current.next
            if current.value == del_val:
                if previous:
                    previous.next = current.next
                else:
                    self.head = self.head.next
        else:
            return None

    def delete_by_pos(self, del_pos):
        if self.head:
            current = self.head
            previous = None
            pos = 1
            while current.next and pos != del_pos:
                previous = current
                current = current.next
                pos += 1
            if pos == del_pos:
                if previous:
                    previous.next = current.next
                else:
                    self.head = self.head.next
        else:
            return None
    
    def get_length(self):
        if self.head:
            current = self.head
            len = 0
            while current:
                current = current.next
                len += 1
            return len
        else:
            return 0


test_ll = LinkedList()
test_ll.display()
print(test_ll.search(2))
test_ll.append("A")
test_ll.append("B")
test_ll.append("C")
test_ll.append("D")
test_ll.insert(3, "Z")
test_ll.display()
print(test_ll.search(1))
test_ll.delete("C")
test_ll.search(5)
test_ll.delete_by_pos(2)
test_ll.display()
print(test_ll.get_length())