class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # smallest subarray such that 
        # sum(subarray) = target
        # i, j = 0,0 
        l, r = 0,0 
        curSum = nums[r]
        if curSum == target:
            return 1
        else:
            best = float('inf')

        while r < len(nums):
            # print(curSum, nums[l:r+1])
            if curSum < target:
                r += 1
                if r < len(nums):
                    curSum += nums[r]
            elif curSum >= target:
                best = min(r-l+1, best)
                curSum -= nums[l]
                l += 1 

        if best == float('inf'):
            return 0
        return best