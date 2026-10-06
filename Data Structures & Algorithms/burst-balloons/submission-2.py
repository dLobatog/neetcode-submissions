class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # f(i)
        # burst:
        #.  - nums[i-1] * nums[i] * nums[i+1] 
        #.  - mark i as visited
        #.  - f(i+1)
        #.  - unmark i as visited
        # skip:
        #.  - f(i+1)
        #. check max(skip, burst)?

        visited = set()
        dp = {}

        def f(remaining):
            best = 0
            if tuple(remaining) in dp:
                return dp[tuple(remaining)]

            for i, balloon in enumerate(remaining):
                prv = 1
                if i - 1 >= 0:
                    prv = remaining[i-1]
                nxt = 1
                if i + 1 < len(remaining):
                    nxt = remaining[i+1]

                coins = prv * balloon * nxt
                del remaining[i]
                best = max(best, coins + f(remaining))
                remaining.insert(i, balloon)

            dp[tuple(remaining)] = best
            return best

        return f(nums)