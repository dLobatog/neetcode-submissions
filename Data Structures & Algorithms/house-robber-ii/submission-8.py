class Solution:
    def rob(self, nums: List[int]) -> int:        
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            dp = [None] * (len(houses) + 1)

            def f(i):
                if i < 0:
                    return 0

                if dp[i] is not None:
                    return dp[i]
                
                prev_rob = f(i-1) + 0 # don't rob
                curr_rob = f(i-2) + houses[i] # rob.. 

                dp[i] = max(prev_rob, curr_rob)
                return dp[i]
                
            return f(len(houses)-1)
        
        return max(
            rob_linear(nums[1:]),
            rob_linear(nums[:-1])
        )
