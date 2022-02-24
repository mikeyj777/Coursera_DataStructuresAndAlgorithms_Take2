import numpy as np
import week1_basic_data_structures.class_examples.doubly_linked_list as LL

class Stack(LL.Hash_Table_Doubly_Linked):


    def push(self, key):
        self.push_front(key)
    
    def top(self):
        a = self.top_front()
        return a.key

    def pop(self):
        a = self.top_front()
        self.pop_front()
        return a.key
    
    def empty(self):

        return self.empty()


    def isBalanced(self, l):

        self.head = None

        for char in l:
            if char in ['(', '[']:
                self.push(char)
            else:
                if self.empty():
                    return False
                top = self.pop()
                if (top == '[' and char != ']') or \
                    (top == '(' and char != ')'):
                    return False
        
        return self.empty()

instr = '([(())])'

stack = Stack()

print(stack.isBalanced(instr))