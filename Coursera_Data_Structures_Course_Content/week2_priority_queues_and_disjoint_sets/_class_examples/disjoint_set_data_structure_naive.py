
class Disjoint_Set:

    smallest = {}

    def __init__(self):
        pass

    def make_set(self,x):
        self.smallest[x] = x

    def find(self, x):
        #return ID of set containing x
        # if x and y lie in same set, find(x) = find(y)
        return self.smallest[x]
    
    def union(self, i, j):
        #merge two sets containing x and y
        #after calling union, a call to find would result in same id for x and y
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id != j_id:
            m = min(i_id, j_id)
            for k in (1,n):
                if self.smallest[k] in {i_id, j_id}:
                    self.smallest[k] = m

    def preprocess(self, maze):
        for c in maze:
            self.make_set(c)
        for c in maze:
            N = self.neighbors(c)
            for n in N:
                self.union(c,n)
    
    def is_reachable(self, a, b):

        return self.find(a) == self.find(b)