class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)
        if p1 == p2:
            return p1
        if self.rank[p1] > self.rank[p2]:
            # increase rank p1
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            # increase rank p1
            self.rank[p2] += 1
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        uf = UnionFind(ROWS * COLS)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '0':
                    continue

                cur = i * COLS + j
                right = i * COLS + (j + 1)
                down  = (i + 1) * COLS + j

                if j + 1 < COLS and grid[i][j + 1] == '1':
                    uf.union(cur, right)

                if i + 1 < ROWS and grid[i + 1][j] == '1':
                    uf.union(cur, down)

        roots = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    roots.add(uf.find(i * COLS + j))

        return len(roots)
                    
                