from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        # longest strictly increasing
        # for all i,j 
        #.  f(di, dj) in all moves, must be < matrix[i,j]
        #   base case - retrun 1

        @cache
        def f(r,c):
            longest = 1
            for dr,dc in moves:
                nr, nc = r+dr, c+dc
                # print(nr,nc)
                if (
                    nr >= 0 and nr < len(matrix) and 
                    nc >= 0 and nc < len(matrix[0]) and
                    matrix[nr][nc] < matrix[r][c]
                ):
                    # print(r,c,matrix[r][c], "moves to", nr,nc,matrix[nr][nc])
                    longest = max(1 + f(nr, nc), longest)
            return longest

        longest = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                longest = max(longest, f(r,c))

        return longest
