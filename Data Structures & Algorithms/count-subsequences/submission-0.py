from functools import cache 

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # to build t from s you can
        # for each letter, in s
        # see if it matches s[i] == t[j]
        # if it does, move forward on i, j (and also, move forward on i only, to cover the caseo f what happens if you skip)
        # if it doesn't, move forward on i only, as you haven't finished
        @cache
        def f(i, j):
            if j >= len(t):
                return 1

            if i >= len(s):
                return 0

            ways = 0
            # print(i, j)
            if s[i] == t[j]:
                ways += f(i+1, j+1)
            ways += f(i+1, j)

            return ways

        return f(0,0)

            