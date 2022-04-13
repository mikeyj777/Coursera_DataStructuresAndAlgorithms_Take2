
class Disjoint_Set:

    parent = {}
    rank = {}

    def __init__(self):
        pass

    def make_set(self,x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        #return ID of set containing x
        # if x and y lie in same set, find(x) = find(y)
        # follow parent path until root is reached (where parent(i) = i)
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    def union(self, i, j):
        #merge two sets containing x and y
        #after calling union, a call to find would result in same id for x and y
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id != j_id:
            if self.rank[i_id] > self.rank[j_id]:
                self.parent[j_id] = i_id
            else:
                self.parent[i_id] = j_id
                if self.rank[i_id] == self.rank[j_id]:
                    self.rank[j_id] += 1   

    def preprocess(self, maze):
        for c in maze:
            self.make_set(c)
        for c in maze:
            N = self.neighbors(c)
            for n in N:
                self.union(c,n)
    
    def is_reachable(self, a, b):

        return self.find(a) == self.find(b)