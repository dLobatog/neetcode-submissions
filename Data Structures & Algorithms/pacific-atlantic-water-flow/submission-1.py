class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # heights represents height above sea level of coordinate
        #  pacific / top-left
        #  atlantic / bottom-right
        #
        # water can flow down up/down/left/righ
        #
        # return all cells [r,c] where the flow goes to both oceans
        # BFS from all cells?
        moves = [[-1,0],[+1,0],[0,+1],[0,-1]]

        def bfs(i, j):
            visited = set()
            q = deque()
            q.append((i,j))
            visited.add((i, j))
            pacific, atlantic = False, False
            while q:
                # print(i, j)
                i, j = q.popleft()
                
                if pacific and atlantic:
                    return True
             
                else:
                    for dx, dy in moves:
                        newx, newy = i+dx, j+dy
                        if (newx, newy) not in visited:
                            if newx < 0 or newy < 0:
                                pacific = True
                            elif newx >= len(heights) or newy >= len(heights[0]):
                                atlantic = True
                            elif heights[newx][newy] <= heights[i][j]:
                                visited.add((newx, newy))
                                q.append((newx, newy))
            return pacific and atlantic

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if bfs(i,j):
                    result.append([i, j])

        return result
