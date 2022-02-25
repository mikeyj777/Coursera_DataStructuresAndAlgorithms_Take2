import numpy as np

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
        # if self.key != None:
        if self.left != None:
            self.left.in_order_traversal()
        print(self.key)
        if self.right != None:
            self.right.in_order_traversal()


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

b_tree.in_order_traversal()

a = 1
