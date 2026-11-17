class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        g = { i:[] for i in range(N) } # i: edges [cost, neighbor]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                g[i].append([dist, j])
                g[j].append([dist, i])

        minH = [[0, 0]] # cost, point
        res = 0
        visited = set()

        while len(visited) != len(points):
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue

            res += cost
            visited.add(node)

            for dist, nei in g[node]:
                if nei not in visited:
                    heapq.heappush(minH, [dist, nei])

        return res