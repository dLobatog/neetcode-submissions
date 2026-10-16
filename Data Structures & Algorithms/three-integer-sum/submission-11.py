class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # one option, make 2sum first with target 0
        #   - 2sum is O(n)
        # to find the 3rd number, iterate over 2sum solutions? 
        # other solution, sort, then do 2sum for sorted solution for each 
        # O(nlogn * n) - both are n**2
        nums.sort()
        result = set()

        for i, n in enumerate(nums):
            j, k = i+1, len(nums)-1
            while j < k:
                targetsum = nums[i]+nums[j]+nums[k]
                if targetsum == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif targetsum > 0:
                    k -= 1
                elif targetsum < 0:
                    j += 1

        return [list(c) for c in result]
