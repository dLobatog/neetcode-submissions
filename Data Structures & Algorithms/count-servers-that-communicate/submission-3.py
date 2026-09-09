class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)

        if p1 == p2:
            return p1

        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1

        self.parent[p2] = p1
        self.size[p1] += self.size[p2]

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # id servers with = (r * COLS + c)
        uf = UnionFind(ROWS*COLS)

        # Union all servers in each row
        for r in range(ROWS):
            first = None
            for c in range(COLS):
                if grid[r][c] == 1:
                    cur = r * COLS + c
                    if first is None:
                        first = cur
                    else:
                        uf.union(first, cur)

        # Union all servers in each column
        for c in range(COLS):
            first = None
            for r in range(ROWS):
                if grid[r][c] == 1:
                    cur = r * COLS + c
                    if first is None:
                        first = cur
                    else:
                        uf.union(first, cur)
        
        # print(uf.parent, uf.size)
        # must go through the uf- and add up the sizes
        total = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    root = uf.find(r * COLS + c)
                    if uf.size[root] >= 2:
                        total += 1

        return total