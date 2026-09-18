class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # if it can be segmented
        # f(i) can it be segmented up to i
        # i == 0 - true
        # else wordDict contains s(0:i)? 
        # if so - True else wordDict contains(lastTrue:i) ? if so True    # else False
        #
        dp = [None] * (len(s) + 1) 
        words = set(wordDict)
        def f(end):
            if end == 0:
                dp[end] = True
                return True
            
            if dp[end] is not None:
                return dp[end]

            for start in range(0, end):
                if s[start:end] in words and f(start):
                    dp[end] = True
                    return True

            dp[end] = False
            return False
       

        return f(len(s))