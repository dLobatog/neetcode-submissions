class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # how about we do toposort
        # once we find last node with indegree > 0... those are candidates for 
        neighbors = defaultdict(list)
        indegree = defaultdict(int)
        
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        visited = set()
        for k, v in indegree.items():
            if v == 1:
                q.append(k)

        while q:
            u = q.popleft()
            visited.add(u)
            
            for n in neighbors[u]:
                if n not in visited:
                    indegree[n] -= 1
                    if indegree[n] == 1:
                        q.append(n)

        # now we would have a few nodes left with indegre > 0:
        # print(indegree, neighbors)
        for u, v in reversed(edges):
            if u not in visited and v not in visited:
                return [u, v]
