class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        
        dp = [[None for _ in range((totalSum//2)+1)] for _ in range(len(nums)+1)]

        def f(i, s1):
            if s1 > totalSum // 2:
                return False

            # print(i, s1, totalSum//2, len(dp), len(dp[0]))
            if dp[i][s1] is not None:
                return dp[i][s1]
            if i == len(nums):
                # print(s1, totalSum)
                return (s1 == totalSum / 2)

            result = f(i+1, s1 + nums[i]) or f(i+1, s1)             
            dp[i][s1] = result
            return result

        return f(0, 0)

