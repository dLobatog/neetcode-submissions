class Solution:
    def numDecodings(self, s: str) -> int:
        # f(end) - "12"
        # say you start f(0) - empty string is 1
        # f(1) - "ways of decoding 1" - is basically ways of decoding
        #.  f(0) if s[:end] between 0 and 26
        # f(2) = f(1) + f(0) ? let's verify
        # f(2) should be number of ways of decoding s[:2]
        # that would be '12' already.
        # we wanna know ways of decoding 'f(1)' for 1, that is fine
        # and for 2, i'm not sure, should we wait for f(3)?
        dp = [None] * (len(s) + 1)

        def f(end):
            if dp[end] is not None:
                return dp[end]

            if end == 0:
                return 1

            cur = s[:end]

            if end == 1:
                if int(cur) > 0 and int(cur) <= 26:
                    return 1
                else:
                    return 0

            ways = 0

            if int(s[end-1:end]) > 0:
                ways += f(end-1) # append cur to end-1 basically
            
            if int(s[end-2:end]) >= 10 and int(s[end-2:end]) <= 26:
                ways += f(end-2)

            dp[end] = ways
            return ways 
            
        return f(len(s))
