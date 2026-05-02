class Graph:
    def __init__(self):
        self.nodes = {}
        
class Node:
    def __init__(self, val):
        self.val = val 
        self.neighbors = set()

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find would do this .
        # otherwise - dfs from every node, marking them as visited, counting
        count = 0 

        visited = set()

        def dfs(node):
            nonlocal visited
            if node.val in visited:
                return
            visited.add(node.val)
            for node in node.neighbors:
                dfs(node)

        graph = Graph()
        
        for i in range(n):
            graph.nodes[i] = Node(val=i)
       
        for source, dest in edges:
            graph.nodes[source].neighbors.add(graph.nodes[dest])
            graph.nodes[dest].neighbors.add(graph.nodes[source])

        for node in graph.nodes.values():
            if node.val not in visited:
                count += 1
                dfs(node)

        return count
                
