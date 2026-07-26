from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = [[+1, 0], [0, +1]]
        goal = (m-1, n-1)
        # we will have to try with a method that allows to open 
        # as many paths as possible

        @cache
        def travel(i: int, j: int) -> int:
            if (i, j) == goal:
                return 1

            results = 0

            if i + 1 < m: # try "down"
                results += travel(i + 1, j)

            if j + 1 < n: # try "right"
                results += travel(i, j + 1)

            return results
            
        return travel(0,0)
            