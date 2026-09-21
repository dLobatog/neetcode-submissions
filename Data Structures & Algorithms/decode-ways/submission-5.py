class Solution:
    def numDecodings(self, s: str) -> int:
        # f(end) - ways of decoding s[:end]
        # base case is. f(0) = 1
        # f(n) depends on f(n-1) and f(n-2) (taking 1 or 2 chars)
        # if s[n-1:n] > 0 - f(n-1) counts, as we're adding 
        #   s[n-1:n] to all ways of decoding f(n-1)
        # if s[n-2:n] >= 10 and <= 26, f(n-2) counts as we're adding
        #.  s[n-2:n] to all ways of decoding f(n-2)
        dp = [None] * (len(s)+1)
        def f(end):
            if dp[end] is not None:
                return dp[end]
            if end == 0:
                return 1
            
            ways = 0
            one_char = int(s[end-1:end])
            if one_char > 0:
                ways += f(end-1)

            
            if end >= 2:
                two_chars = int(s[end-2:end])
                if two_chars >= 10 and two_chars <= 26:
                    ways += f(end-2)

            dp[end] = ways
            return ways

        return f(len(s))
