class Node:
    def __init__(self, id):
        self.id = id
        self.children = {}
    
    def __str__(self):
        return f"{self.id} - {self.children}"

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what defines a tree?
        # A tree has exactly n-1 edges vs nodes. 
        # if there are n edges, at least 1 is creating a cycle
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
        # bfs:
        q = deque()
        q.append(0)
        visited = {}
        while q:
            cur = q.popleft()
            visited[cur] = True
            for child in graph[cur]:
                if child not in visited:
                    q.append(child)
        
        return len(visited) == n
            
            
