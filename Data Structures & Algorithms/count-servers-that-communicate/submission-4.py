class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # id servers with = (r * COLS + c)
        row_count = defaultdict(int)
        col_count = defaultdict(int)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (row_count[r] > 1 or col_count[c] > 1):
                    total += 1

        return total
