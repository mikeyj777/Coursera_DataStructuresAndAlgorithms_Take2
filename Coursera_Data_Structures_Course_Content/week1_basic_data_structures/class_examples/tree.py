import numpy as np

class Tree:

    key = None

    def height(self):
        pass


class Binary_Tree(Tree):

    def add_left(self, key):
        self.left = Binary_Tree()
        self.left.key = key

    def add_right(self, key):
        self.right = Binary_Tree()
        self.right.key = key
    
    def height(self):
        if self.left == None and self.right == None:
            return 0
        return 1 + max(self.left.height,self.right.height)
