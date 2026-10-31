from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            movements = [
                [1, 0], [-1,0] , [0,1], [0,-1]
            ]
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"
            while q:
                r, c = q.popleft()
                
                
                for dr, dc in movements:
                    new_r, new_c = dr + r, dc + c
                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == "1":
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = "0"

            return 

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": # island found, let's mark all as seen
                    count += 1
                    bfs(r, c)

        # O(rows x columns) time 
        # O(1 space) - we reuse the input lol

        return count

