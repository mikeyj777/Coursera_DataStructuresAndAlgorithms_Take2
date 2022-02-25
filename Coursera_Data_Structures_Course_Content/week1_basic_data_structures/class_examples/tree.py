import numpy as np

class Tree:

    key = None

    def height(self):
        pass


class Binary_Tree(Tree):

    left = None
    right = None

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


b_tree = Binary_Tree()

b_tree.add_left('a')
b_tree.add_right('b')
b_tree.left.add_left('aa')
b_tree.right.add_left('ba')
b_tree.right.add_right('ba')

b_tree.right.right.add_left('baa')

print(b_tree.height())

a = 1
