class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return p

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)
        if p1 == p2:
            return p1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # start from borders
        # if found a 'O' do dfs and mark as S
        # after done, mark every non 'S' as 'X'
        # last round, mark 'S' as 'O' and return
        ROWS, COLS = len(board), len(board[0])
        MOVES = [[-1, 0], [+1, 0], [0, -1], [0, +1]]
        visited = set()

        def in_bounds(r, c):
            return r < ROWS and c < COLS and c >= 0 and r >= 0

        def dfs(r, c):
            if not in_bounds(r,c) or (r,c) in visited:
                return
            
            board[r][c] = 'S' # for saved
            visited.add((r,c))

            for dy, dx in MOVES:
                y = dy + r
                x = dx + c
                if in_bounds(y, x) and board[y][x] == 'O':
                    dfs(y, x)

        # how to find first row, last row, first col, last col
        for r in [0, ROWS-1]:
            for c in range(COLS):
                if board[r][c] == 'O':
                    dfs(r,c)
        for r in range(ROWS):
            for c in [0, COLS-1]:
                if board[r][c] == 'O':
                    dfs(r,c)

        # print('board post dfs', board)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                

        