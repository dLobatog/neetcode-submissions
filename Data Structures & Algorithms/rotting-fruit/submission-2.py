class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # This state is impossible, when there is are fresh fruits
        # without connections to the rest of the grid, where there are rotten fruits
        # 
        # To compute the minutes, we can think about the rotten fruits, as sources to 
        # do BFS. 
        # 
        # Every minute, we should do one more level of BFS, from each rotten fruit to
        # the up/down/right/left positions of it.
        #
        # The amount of levels needed until we run out of options (running out = no rotten
        # fruits during this process => finished) is exactly the amount of minutes
        #
        # If the amount of levels is 0, then return -1
        # [2,1,1]
        #.[0,1,1]
        # [1,0,1]

        moves = [[+1, +0], [-1, +0], [+0, -1], [+0, +1]]

        # need to enqueue first all "2"
        q = deque()
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0)) # append position
                    visited.add((i, j))

        level = 0
        while q:
            i, j, level = q.popleft()
            # print("q, visited", q, visited)
            for dx, dy in moves:
                new_i, new_j = i + dx, j + dy
                if (new_i, new_j) not in visited and new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0])  and grid[new_i][new_j] == 1:
                    # check if it's a fresh fruit
                    print(new_i, new_j)
                    visited.add((new_i, new_j))
                    q.append((new_i, new_j, level + 1))

     
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1

        return level