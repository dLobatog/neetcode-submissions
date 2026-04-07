class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        # update 
        running_sum = 0
        for num in nums:
            running_sum += num
            result = max(result, running_sum)
            if running_sum < 0:
                running_sum = 0

        return result
                

        