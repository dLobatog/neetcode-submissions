class Node:
    def __init__(self, val):
        self.neighbors = {}
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # time it takes for signal to travel to 
        g = {}
        for i in range(1, n+1):
            g[i] = Node(i)
        for source, target, time in times: 
            g[source].neighbors[target] = time

        # if we send from k, how long to reach all others
        start = g[k]
        visited = set()
        q = []
        heapq.heappush(q, (0, start))
        time = 0
        while q:
            elapsed, curr = heapq.heappop(q)
            if curr.val in visited:
                continue
            visited.add(curr.val)
            time = max(time, elapsed)

            if len(visited) == n:
                # print(visited)
                return time
            
            for id, edge_time in curr.neighbors.items():
                if id not in visited: 
                    heapq.heappush(q, (elapsed + edge_time, g[id]))

        return -1


            



