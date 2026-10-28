class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        perimeter += 1
                    elif grid[nr][nc] == 0:
                        perimeter += 1


        return perimeter