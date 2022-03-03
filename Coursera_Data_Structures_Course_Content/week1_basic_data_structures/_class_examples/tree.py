import numpy as np
import copy
from myqueue import Queue

class Tree:

    key = None

    def height(self):
        pass


class Binary_Tree(Tree):

    left = None
    right = None

    def set_root(self):
        self.key = 'root'

    def add_left(self, key):
        self.left = Binary_Tree()
        self.left.key = key

    def add_right(self, key):
        self.right = Binary_Tree()
        self.right.key = key
    
    def height(self):
        if self.left == None:
            if self.right == None:
                return 0
            return 1 + self.right.height()

        if self.right == None:
            if self.left == None:
                return 0
            return 1 + self.left.height()

        return 1 + max(self.left.height(), self.right.height())

    def size(self):
        if self.left == None:
            if self.right == None:
                return 1
            return 1 + self.right.size()

        if self.right == None:
            if self.left == None:
                return 1
            return 1 + self.left.size()
        
        return 1 + self.left.size() + self.right.size()

    def in_order_traversal(self):
        
        if self.left != None:
            self.left.in_order_traversal()
        print(self.key)
        if self.right != None:
            self.right.in_order_traversal()
    
    def pre_order_traversal(self):
        if self.key != None:
            print(self.key)
        if self.left != None:
            self.left.pre_order_traversal()
        if self.right != None:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left != None:
            self.left.post_order_traversal()
        if self.right != None:
            self.right.post_order_traversal()
        if self.key != None:
            print(self.key)

    def level_traversal(self):
        if self.left != None or self.right != None:
            q = Queue()
            q.enqueue(self)
            while not q.empty():
                node = q.dequeue()
                print(node.key)
                if node.left != None:
                    q.enqueue(node.left)
                if node.right != None:
                    q.enqueue(node.right)



b_tree = Binary_Tree()

b_tree.key = 'Les'
b_tree.add_left('Cathy')
b_tree.left.add_left('Alex')
b_tree.left.add_right('Frank')
b_tree.add_right('Sam')
b_tree.right.add_left('Nancy')
b_tree.right.add_right('Violet')
b_tree.right.right.add_left('Tony')
b_tree.right.right.add_right('Wendy')

b_tree.level_traversal()

a = 1
