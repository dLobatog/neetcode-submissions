class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # once you find 1 you need to dfs on it
        # count X for the amount of walls or non-1s around
        # continue until finished

        visited = set()
        count = 0

        def dfs(r,c):
            nonlocal visited, count

            visited.add((r, c))

            directions = [
                [1,  0],
                [-1, 0],
                [0, -1],
                [0,  1]
            ]

            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                    if (new_r, new_c) in visited:
                        continue
                    elif grid[new_r][new_c] == 0:
                        count += 1
                    elif grid[new_r][new_c] == 1:
                        dfs(new_r, new_c)
                else: 
                    count += 1 # wall

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return count

            