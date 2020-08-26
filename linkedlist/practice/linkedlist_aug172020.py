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
    
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def merge_sorted(self, llist2):
        p = self.head
        q = llist2.head
        s = None

        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.value <= q.value:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        
        while p and q:
            if p.value <= q.value:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if not p:
            s.next = q
        if not q:
            s.next = p
        
        return new_head
    
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()
        while cur:
            if cur.value in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.value] = 1
                prev = cur 
            cur = prev.next

    
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
print("++++++++++++++++++++++++++")
test_ll.reverse_iterative()
test_ll.display()

print(test_ll.len_iterative())
print(test_ll.len_recursive(test_ll.head))
print("++++++++++++++++++++++++++")
num_ll = LinkedList()
num_ll.append(1)
num_ll.append(5)
num_ll.append(6)
num_ll.append(8)
num_ll2 = LinkedList()
num_ll2.append(2)
num_ll2.append(3)
num_ll2.append(4)
num_ll2.append(7)
print("++++++++++++++++++++++++++")
num_ll.merge_sorted(num_ll2)
num_ll.display()
print("++++++++++++++++++++++++++")
num_ll3 = LinkedList()
num_ll3.append(1)
num_ll3.append(2)
num_ll3.append(2)
num_ll3.append(3)
num_ll3.append(4)
num_ll3.append(3)
num_ll3.remove_duplicates()
num_ll3.display()