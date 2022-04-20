
class Disjoint_Set:

    parent = {}
    rank = {}

    def __init__(self):
        pass

    def make_set(self,x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, i):
        #return ID of set containing x
        # if x and y lie in same set, find(x) = find(y)
        # follow parent path until root is reached (where parent(i) = i)
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
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
                #if trees are of the same height, hanging j on i will make it one node taller.
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
    
    def get_height(self, i):
        height = 0
        while i != self.parent[i]:
            height += 1
            i = self.parent[i]
        return height
        

dj = Disjoint_Set()
# for i in range(1,13):
#     dj.make_set(i)
# dj.union(2, 10)
# dj.union(7, 5)
# dj.union(6, 1)
# dj.union(3, 4)
# dj.union(5, 11)
# dj.union(7, 8)
# dj.union(7, 3)
# dj.union(12, 2)
# dj.union(9, 6)

# n = 5

# for i in range(1,n+1):
#     dj.make_set(i)
# for i in range(1, n):
#     dj.union(i, i+1)

for i in range(1,61):
  dj.make_set(i)
for i in range(1,31):
  dj.union(i, 2*i)
for i in range(1,21):
  dj.union(i, 3*i)
for i in range(1,13):
  dj.union(i, 5*i)
for i in range(1,61):
  dj.find(i)

max_height = 0
for k in dj.parent.keys():
    h = dj.get_height(k)
    if h > max_height:
        max_height = h
        print(max_height)

a = 1