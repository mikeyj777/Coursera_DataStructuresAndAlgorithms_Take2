import numpy as np
import copy

class Node:

    key = None
    next = None
    prev = None

class Hash_Table_Doubly_Linked:

    head = None
    tail = None

    def push_front(self, key):
        node = Node()
        node.key = key
        node.next = copy.deepcopy(self.head)
        self.head = copy.deepcopy(node)

        if self.tail == None:
            self.tail = self.head
    
    def pop_front(self):

        if self.head == None:
            print("Error - Can't pop from empty list")
        else:
            self.head = copy.deepcopy(self.head.next)
    
    def push_back(self, key):

        new_node = Node()
            
        new_node.key = key
        
        if self.tail == None:
            self.tail = self.head = new_node

        else:
            
            self.tail.next = new_node
            new_node.prev = self.tail
            # temp_tail = copy.deepcopy(self.tail)
            
            self.tail = copy.deepcopy(new_node)
    
    def pop_back(self):
        if self.head == None:
            print("Error - Can't pop from empty list")
        
        else:
            if id(self.head) == id(self.tail):
                self.head = self.tail = None
            else:
                p = self.tail.prev
                self.tail = p
                self.tail.next = None
    
    def add_after(self, node, key):
        node2 = Node()
        node2.key = key
        node2.next = node.next
        node2.prev = node

        node.next = node2

        if node2.next != None:
            node2.next.prev = node2
        if id(self.tail) == id(node):
            self.tail = node2
    
    def add_before(self, node, key):
        node2 = Node()
        node2.key = key
        node2.next = node

        p = node.prev
        p.next = node2
