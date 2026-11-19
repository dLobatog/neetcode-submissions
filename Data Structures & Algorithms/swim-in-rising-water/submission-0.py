class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        movements = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        # bfs getting to the end
        goal = (len(grid)-1, len(grid[0])-1)
        q = []
        visited = set()
        q.append((grid[0][0], (0,0))) # water_level, store point
        minCost = len(grid) * len(grid[0])
        while q:
            water_level, point = heapq.heappop(q)

            if point in visited:
                continue
            
            visited.add(point)

            if point == goal:
                minCost = min(minCost, water_level)
                return minCost

            for dr, dc in movements:
                new_r, new_c = dr+point[0], dc+point[1]
                if (
                    0 <= new_r < len(grid) and
                    0 <= new_c < len(grid[0]) and 
                    (new_r, new_c) not in visited
                    ):
                    # add it and move taking +1 cost if water level > cost
                    # add it and move taking +"water_level-cost" cost if cost < water_level as we need to wait
                    elevation = grid[new_r][new_c]
                    new_time = max(water_level, grid[new_r][new_c])
                    heapq.heappush(q, (new_time, (new_r, new_c)))
                    
        
        # print(minCost)
        return minCost



