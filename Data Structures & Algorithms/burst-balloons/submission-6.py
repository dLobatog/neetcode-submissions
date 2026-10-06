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
        dp = {}

        def f(l, r):
            if l > r: 
                return 0
            if (l,r) in dp:
                return dp[(l, r)]
            
            best = 0 
            # print(l ,r)
            for i in range(l, r+1):
                balloon = nums[l-1] * nums[i] * nums[r+1]
                best = max(
                    best, 
                    f(l, i-1) + balloon + f(i+1, r)
                )

            dp[(l, r)] = best
            return best
        
        nums = [1] + nums + [1]
        return f(1, len(nums)-2)

        # # too many different states
        # def f(remaining):
        #     best = 0
        #     if tuple(remaining) in dp:
        #         return dp[tuple(remaining)]

        #     for i, balloon in enumerate(remaining):
        #         prv = remaining[i-1] if i > 0 else 1
        #         nxt = remaining[i+1] if i < len(remaining)-1 else 1

        #         coins = prv * balloon * nxt
        #         del remaining[i]
        #         best = max(best, coins + f(remaining))
        #         remaining.insert(i, balloon)

        #     dp[tuple(remaining)] = best
        #     return best

        # return f(nums)