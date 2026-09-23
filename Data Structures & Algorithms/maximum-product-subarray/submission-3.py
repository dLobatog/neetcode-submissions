class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # f(i) = highest product subarray ending on i
        # g(i) = highest product subarray ending on i
        # -4, -3, -2...
        # i = 1:
        #   prev_max = max(-12, -12, -3) = -3
        #   prev_min = min(-12, -12, -3) = -12
        # i = 2
        #   prev_max = max(-6, 24, -2) = 24
        #   prev_min = min(-6, 24, -2) = -6

        best, prev_max, prev_min = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)): 
            orig_prev_max = prev_max
            prev_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
            prev_min = min(orig_prev_max * nums[i], prev_min * nums[i], nums[i])
            best = max(prev_max, best)

        return best
