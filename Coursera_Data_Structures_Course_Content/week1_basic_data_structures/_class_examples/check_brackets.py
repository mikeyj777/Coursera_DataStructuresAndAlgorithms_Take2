# python3
import copy
from turtle import position

openings = ['(', '[', '{']
closings = [')', ']', '}']

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
        return self.head.key
    
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
        
        return self.tail.key


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

class Stack(Hash_Table_Doubly_Linked):


    def push(self, key):
        self.push_front(key)
    
    def top(self):
        a = self.top_front()
        return a

    def pop(self):
        a = self.top_front()
        self.pop_front()
        return a


    def isBalanced(self, l):

        self.head = None

        for char in l:
            if char in ['(', '[']:
                self.push(char)
            else:
                if self.empty():
                    return False
                if char in [')', ']']:
                    top = self.pop()
                    if (top == '[' and char != ']') or \
                        (top == '(' and char != ')'):
                        return False
        
        return self.empty()
    
    def find_mismatch(self, l):

        self.head = None
        posn = 0

        for char in l:
            posn += 1
            if char in openings:
                self.push([char, posn])
            else:
                # if self.empty():
                #     return posn
                if char in closings:
                    top = self.pop()[0]
                    if (top == '[' and char != ']') or \
                        (top == '(' and char != ')') or \
                        (top == '{' and char != '}') :
                        return posn
        
        if self.head == None:
            return 0
        
        return self.head.key[1]


def main():
    text = input()
    stack = Stack()
    mismatch = stack.find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == 0:
        mismatch = 'Success'

    print(mismatch)

if __name__ == "__main__":
    main()
