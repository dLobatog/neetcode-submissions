class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # f(i) = the minimum number of extra characters needed to process the remaining string s[i:].
        words = set(dictionary)
        dp = [None] * len(s)

        def f(i):
            if i == len(s):
                return 0
            
            if dp[i]:
                return dp[i]

            # Option 1: count this char as extra and skip
            best = 1 + f(i + 1)

            # Option 2: match with the longest possible string
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    best = min(best, f(j + 1))

            dp[i] = best
            return best
            
        return f(0)