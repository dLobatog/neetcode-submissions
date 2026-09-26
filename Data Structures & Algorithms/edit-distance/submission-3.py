from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # can add a character
        # can remove a character
        # can replace a character
        # 3 operations at any position
        @cache
        def f(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return f(i+1, j+1)
            else:
                add = f(i+1, j) # add a char
                delete = f(i, j+1) # delete a char 
                replace = f(i+1, j+1) # replace?
                # print(add, delete, replace, i, j)
                result = min(add, delete, replace) + 1
                return result

        return f(0, 0)
