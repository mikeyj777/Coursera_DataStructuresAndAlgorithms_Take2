#python3
import numpy as np
from collections import deque
import sys


class StackWithMax(deque):
    
    max_val = -np.inf

    def __init__(self):
        self.max_stack = deque()

    def Push(self, a):
        self.append(a)
        if a >= self.max_val:
            self.max_val = a
            self.max_stack.append(a)


    def Pop(self):
        # assert(len(self.__stack))
        a = self.pop()
        if a == self.max_val:
            l = len(self.max_stack)
            for _ in range(min(l, 2)):
                b = self.max_stack.pop()
            self.max_val = b
            self.max_stack.append(b)


    def Max(self):
        # assert(len(self.__stack))
        return self.max_val



if __name__ == '__main__':
    stack = StackWithMax()



    # for query in queries:

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
            
        elif query[0] == "pop":
            stack.Pop()
            
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
