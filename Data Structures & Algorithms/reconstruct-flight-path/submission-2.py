class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            g[src].append(dst)

        res = []

        def dfs(src):
            while g[src]: # while there are tickets from this airport, use them
                dst = g[src].pop()
                dfs(dst)

            res.append(src)

        dfs('JFK')

        return res[::-1]