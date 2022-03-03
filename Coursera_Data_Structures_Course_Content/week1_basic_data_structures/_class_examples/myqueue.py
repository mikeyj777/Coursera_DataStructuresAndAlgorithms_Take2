import numpy as np
import doubly_linked_list as LL

class Queue(LL.Hash_Table_Doubly_Linked):
    
    def enqueue(self, key):
        self.push_back(key)
    
    def dequeue(self):
        a = self.top_front()
        self.pop_front()
        return a

    def empty(self):
        return self.head == None and self.tail == None