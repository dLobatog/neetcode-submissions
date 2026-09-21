class Solution:
    def rob(self, nums: List[int]) -> int:
        # robbing - cannot rob 2 adjacent houses
        # houses are setup in a circle
        #   - this means effectively len(nums)-1 and 0 are consecutive
        # f(i): max $ can be robbed up to i
        # i == 0: you may rob nums[0], no alerts
        # i == 1: you may rob max(nums[0], nums[1]) - they're consecut
        # i > 1: max(f(i-1), f(i-2) + nums[i])
        def f(i):
            if dp[i] is not None:
                return dp[i]
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            prev_rob = f(i-1) + 0 # don't rob
            curr_rob = f(i-2) + nums[i] # rob.. 
            result = max(prev_rob, curr_rob)

            dp[i] = result
            return result

        # a = f(len(nums)-1)
        # [3,4,3] - nozero = True - 4
        # [3,4,3] - nozero 

        if len(nums) == 1:
            return nums[0]
        
        dp = [None] * len(nums)
        orig_nums = nums.copy()
        nums = orig_nums[1:]
        a = f(len(nums)-1)
        nums = orig_nums[:-1]
        dp = [None] * len(nums)
        b = f(len(nums)-1)
        return max(a, b)


