class Node:
    def __init__(self):
        self.in_edges = 0
        self.neighbors = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # toposort of course
        # graph:
        #.   each node contains: next edges
        #.        incoming edges?
        g = {}
        for c in range(numCourses):
            g[c] = Node()

        for dest, src in prerequisites:
            g[src].neighbors.append(dest)
            g[dest].in_edges += 1

        q = deque()
        visited = set()
        # find courses without any incoming edge
        for node in g.keys():
            if g[node].in_edges == 0:
                q.append(node)
                visited.add(node)

        while q:
            node = q.popleft()

            # traverse neighbors
            for neighbor in g[node].neighbors:
                g[neighbor].in_edges -= 1

                if neighbor not in visited and g[neighbor].in_edges == 0:
                    q.append(neighbor)
                    visited.add(neighbor)

        return len(visited) == numCourses
