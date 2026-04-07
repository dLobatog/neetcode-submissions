class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
         
        directions = [
            (-1, 0), # up
            (+1, 0), # down
            (0, -1), # left
            (0, +1) # right
        ] 

        def dfs(x, y):
            nonlocal directions, visited, grid

            visited[x][y] = True 
            
            for dx, dy in directions:
                if x+dx < 0 or x+dx > len(grid) - 1 or y+dy < 0 or y+dy > len(grid[0]) - 1:
                    continue
                if grid[x+dx][y+dy] == '1' and visited[x+dx][y+dy] == False:
                    dfs(x+dx, y+dy)

        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == False:
                    dfs(i, j)
                    print(i,j)
                    islands += 1

        return islands

        