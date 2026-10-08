class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        h = [(0, src)]
        g = defaultdict(list)
        for i in range(n):
            g[i] = [] 
        for u, v, w in edges:
            g[u].append((v, w))
        
        result = {}
        visited = set()
        visited.add(src)
        while h:
            distance, node = heapq.heappop(h)  
            if node in result:
                continue

            result[node] = distance

            for neighbor, weight in g[node]:
                heapq.heappush(h, (weight + distance, neighbor))
                
        for i in range(n):
            if i not in result:
                result[i] = -1

        return result