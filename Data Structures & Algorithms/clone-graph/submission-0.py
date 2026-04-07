"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = defaultdict(int)

        def clone(clonedNode):
            nonlocal visited

            if not clonedNode:
                return None
            if visited[clonedNode.val]:
                return visited[clonedNode.val]

            newNode = Node(val=clonedNode.val)
            neighbors = []
            visited[clonedNode.val] = newNode

            for neighbor in clonedNode.neighbors:
                newNeighbor = clone(neighbor)
                if newNeighbor:
                    neighbors.append(newNeighbor)

            newNode.neighbors = neighbors 
            return newNode

        return clone(node)
