import functools

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @functools.cache
        def dfs(i, j):
            if i == len(text1) and j == len(text2):
                return 0 # must stop
            elif i == len(text1):
                return dfs(i, j+1)
            elif j == len(text2):
                return dfs(i+1, j)

            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            else:
                return max(dfs(i+1, j), dfs(i, j+1))

        return dfs(0, 0)
