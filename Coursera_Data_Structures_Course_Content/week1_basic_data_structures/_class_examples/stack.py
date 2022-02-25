import numpy as np
import doubly_linked_list as LL

class Stack(LL.Hash_Table_Doubly_Linked):


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

instr = '(4 + [ 15* ( a chipmunk / ( 2**3 ) / 45 ) + 20] * 8)'

stack = Stack()

print(stack.isBalanced(instr))