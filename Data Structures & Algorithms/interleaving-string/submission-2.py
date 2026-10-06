from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # abs(n - m) - difference of substrings is at most 1
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def f(i, j, k):
            if k >= len(s3):
                return True

            s1_match = False
            if i < len(s1) and s3[k] == s1[i]:
                s1_match = f(i+1, j, k+1)
            
            s2_match = False
            if j < len(s2) and s3[k] == s2[j]:
                s2_match = f(i, j+1, k+1)

            result = s1_match or s2_match
            return result

        return f(0,0,0)
                