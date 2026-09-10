class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = {}


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = {}
        for i in range(n):
            g[i] = Node(i)

        for u, v, price in flights:
            g[u].neighbors[v] = price

        h = []
        heapq.heappush(h, (0, 0, src))
        best = [[float("inf")] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        while h:
            cost_so_far, flights, node_id = heapq.heappop(h)
            best[node_id][flights] = min(best[node_id][flights], cost_so_far)
            print(cost_so_far, flights, node_id)

            if node_id == dst:
                return cost_so_far

            if cost_so_far > best[node_id][flights]:
                continue

            if flights > k:
                # pop everything seen until here? lol
                continue

            for neigh_id, price in g[node_id].neighbors.items():
                heapq.heappush(h, (cost_so_far + price, flights + 1, neigh_id))

        return -1




