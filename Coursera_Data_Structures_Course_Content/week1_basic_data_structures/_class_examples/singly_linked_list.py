import numpy as np
import copy

class Node:
    
    next = None
    key = None
    value = None

class Hash_Table_Singly_Linked:

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
            self.tail = self.head = node

            while node.next != None:
                node = node.next
            
            node.next = new_node
        else:
            
            self.tail.next = new_node

            # temp_tail = copy.deepcopy(self.tail)
            
            self.tail = copy.deepcopy(new_node)
    
    def pop_back(self):
        if self.head == None:
            print("Error - Can't pop from empty list")
        
        else:
            if id(self.head) == id(self.tail):
                self.head = self.tail = None
            else:
                p = self.head
                while p.next.next != None:
                    p = p.next
                p.next = None
                self.tail = p 
    
    def add_after(self, node, key):
        node2 = Node()
        node2.key = key
        node2.next = node.next
        node.next = node2
        if id(self.tail) == id(node):
            self.tail = node2
    
    def add_before(self, node, key):
        node2 = Node()
        node2.key = key
        node2.next = node

        p = self.head
        while id(p.next) != id(node):
            p = p.next
            if p == None:
                print('Error.  Node not found.')
                break
    
        if p != None:
            p.next = node2


        

    
