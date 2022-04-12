import numpy as np


#max_size = max elem no in heap
#size = sz of heap
#H[1..max_size] = arr of len max_size where heap occupies first "size" elements

class Bin_Tree_Complete:

    h = []
    max_size = 0
    size = 0

    def __init__(self, max_size, size):
        self.max_size = max_size
        self.size = size
        self.h = np.empty(self.max_size+1)

    def get_parent(self, i):
        return i//2
    
    def get_left_child(self, i):
        return 2*i

    def get_right_child(self, i):
        return 2*i + 1
    
    def sift_up(self, i):
        parent = self.get_parent(i)
        while i > 1 and self.h[parent] < self.h[i]:
            self.swap(parent, i)    
            i = parent
            parent = self.get_parent(i)

    def swap(self, first, second):
        self.h[first], self.h[second] = self.h[second], self.h[first]
    
    def sift_down(self, i):
        max_index = i
        l = self.get_left_child(i)
        if l <= self.size and self.h[l] > self.h[max_index]:
            max_index = l
        r = self.get_right_child(i)
        if r <= self.size and self.h[r] > self.h[max_index]:
            max_index = r
        if i != max_index:
            self.swap(i, max_index)
            self.sift_down(max_index)
    
    def insert(self, p):
        if self.size < self.max_size:
            self.size += 1
            self.h[self.size] = p
            self.sift_up(self.size)
    
    def extract_max(self):
        result = self.h[1]
        self.h[1] = self.h[self.size]
        self.size -= 1
        self.sift_down(1)
        return result
    
    def remove(self, i):
        self.h[i] = np.inf
        self.sift_up(i)
        self.extract_max()
    
    def change_priority(self, i, p):
        oldp = self.h[i]
        self.h[i] = p
        if p > oldp:
            self.sift_up(i)
        else:
            self.sift_down(i)
    

class Heap_for_Sorting(Bin_Tree_Complete):

    def __init__(self, A):
        self.A = A
        max_size = len(A)
        super().__init__(max_size = max_size, size = 0)


    def build_heap(self):
        self.size = len(self.A)
        self.h = self.A
        self.h.insert(0, None)
        for i in range((self.size - 1) // 2, 0, -1):
            self.sift_down(i)


    def heap_sort(self):
        self.build_heap()
        for i in range(self.max_size-1, 0, -1):
            self.h[1], self.h[self.size] = self.h[self.size], self.h[1]
            self.size -= 1
            self.sift_down(1)
    
    def output(self):
        print(self.A[1:])

dat_heap = Heap_for_Sorting([8,4,5,10,1,-2])
dat_heap.heap_sort()
dat_heap.output()
