class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # no cycles in the graph
        # we have numCourses always - so we can initialize the graph 
        # do a kind of topological sort - first find sources (no incoming edges) - then move on
        # for example in [[0, 1]]
        #   - we go through all sources and add them to a queue (BFS style)
        #.  - then we pop them, and as we pop them, we add the outgoing nodes 
        #.  - since courses are labeled - we keep visited courses - if we visit twice, return false
        if len(prerequisites) == 0:
            return True

        visited = defaultdict(bool)

        class Node:
            def __init__(self, val=None, outgoing=[]):
                self.val = val 
                self.in_degree = 0
                self.outgoing = outgoing

        graph = {}

        for i in range(numCourses):
            graph[i] = Node(val=i, outgoing=[])

        for source_id, dest_id in prerequisites: 
            graph[source_id].outgoing.append(dest_id)
            graph[dest_id].in_degree += 1

        q = deque()

        # find nodes with no incoming edges:
        for val, node in graph.items():
            if node.in_degree == 0:
                q.append(node)

        if len(q) == 0: # no nodes to begin with 
            return False

        visited = 0

        # we got the sources. 
        while q:
            node = q.popleft()
            visited += 1
            print("popped", node.val, visited)
            
            for neighbor in node.outgoing:
                graph[neighbor].in_degree -= 1
                if graph[neighbor].in_degree == 0:
                    q.append(graph[neighbor])

        # for value in visited.values():
        #     if value is False:
        #         return False

        return visited == numCourses

