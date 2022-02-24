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
    
    def top_front(self):
        return self.head
    
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
    
    def top_back(self):

        #return back item
        if self.tail == None:
            self.tail = self.head
        
        if self.head == None:
            print("Error:  Can't Pop from Empty list")
        
        return self.tail


    def pop_back(self):

        #remove back item

        if self.head == None:
            print("Error - Can't pop from empty list")
        
        else:
            if id(self.head) == id(self.tail):
                self.head = self.tail = None
            else:
                p = self.tail.prev
                self.tail = p
                self.tail.next = None
        
    def find(self, key):

        p = self.head

        while p.key != key:
            p = p.next

        return p.key == key

    def erase(self,key):
        
        if self.head.key == key:
            self.pop_front()
        elif self.tail.key == key:
            self.pop_back()
        else:
            p = self.head

            while p.key != key:
                p = p.next

            if p.key == key:
                p.prev.next = p.next
                p.next.prev = p.prev
            else:
                print('Error.  Key not found.')

    def empty(self):

        return self.head == None 


        
        
    
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
