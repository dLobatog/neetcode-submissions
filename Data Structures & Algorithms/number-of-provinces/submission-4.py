class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)

        if p1 == p2: # same parent
            return p1 
        
        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1 

        self.parent[p2] = p1
        self.size[p1] += self.size[p2]
    



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # if a is connected with b and b with c, then they're 
        # connected indirectly 
        # a province is a group of directly or indirectly connected
        # return number of provinces
        # could do union-find? 
        # parent 
        # size
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        provinces = set()
        for city in range(n):
            provinces.add(uf.find(city))


        # print(uf.parent, uf.size)
        return len(provinces)

        