# python3

import sys
import threading

class Node:
    child = None
    parent = None
    isRoot = False
    index = None



def compute_height(n, parents):
    # Replace this code with a faster implementation
    nodes = []
    for i in range(n):
        node = Node()
        node.index = i
        if parents[i] == -1:
            node.isRoot = True
        nodes.append(node)

    for i in range(n):
        if parents[i] != -1:
            nodes[parents[i]].child = nodes[i]
            nodes[i].parent = nodes[parents[i]]
    
    max_height = 0
    for i in range(n):
        height = 1
        p = nodes[i]
        while p.child != None:
            height += 1
            p = p.child
        max_height = max(height, max_height)
            


    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))

    # parents = [4, -1, 4, 1, 1]

    print(compute_height(len(parents), parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
