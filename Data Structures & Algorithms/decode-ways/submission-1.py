class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [None] * (len(s) + 1)
        def f(end):
            if dp[end] is not None:
                return dp[end]
            if end == 0:
                return 1

            best = 0
            for start in range(0, end):
                if s[start] == '0':
                    continue
                test = int(s[start:end])
                # will test all ways to decode this number but these 
                # are gonna be way too many
                #
                if test > 0 and test <= 26:
                    best += f(start)
                    # this counts how many s[:start] ways can be decoded
                
            dp[end] = best
            return best

        return f(len(s))


            
