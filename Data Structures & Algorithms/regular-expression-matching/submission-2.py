class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def f(i, j):
            if (i,j) in memo:
                return memo[(i, j)]
            if j >= len(p):
                return i >= len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                #      don't use                use
                res = f(i, j+2) or (match and f(i+1, j))
            else:
                res = match and f(i+1, j+1)
                
            memo[(i, j)] = res
            return res

        memo = {}
        return f(0,0)

