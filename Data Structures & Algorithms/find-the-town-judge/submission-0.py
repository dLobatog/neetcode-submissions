class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 1 to n people
        # judge trusts nobody (no outgoing edges)
        # everybody trusts the judge (incoming edges = n - 2)
        # only 1 person satisfies both
        # ok model as edges
        outgoing = {}
        incoming = {}
        for i in range(1, n +1):
            outgoing[i] = set()
            incoming[i] = 0
        
        for u, v in trust:
            outgoing[u].add(v)
            incoming[v] += 1

        judge = None
        for k, v in outgoing.items():
            if len(v) == 0:
                if judge is not None:
                    return -1 # can't have 2 judges
                judge = k

        
        # print(incoming[judge], outgoing[judge])
        if judge is None or incoming[judge] != n-1:
            return -1
        
        return judge
