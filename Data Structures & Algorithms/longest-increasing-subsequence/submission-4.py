class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #. [3,1,2,5,4]
        #. take 3, continue 
        #. don't take 3, continue
        #.      3.         -
        #.      -          1     
        #       -          2
        #       5          5
        #       -          - 
        dp = [{} for _ in range(len(nums)+1)]
        def f(i, last):
            if i == len(nums):
                return 0
            
            if last in dp[i]:
                return dp[i][last]

            # print(i, nums[i], last)
            take = 0
            if nums[i] > last:
                take = 1 + f(i + 1, nums[i]) 
        
            skip = f(i+1, last)

            dp[i][last] = max(skip, take)
            # print(skip, take)
            return dp[i][last]

        return f(0, -float('inf'))