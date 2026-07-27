class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums)-1
            while l < r and r < len(nums):
                target = nums[i] + nums[l] + nums[r]
                if (target == 0):
                    result.add(
                        tuple(sorted((nums[i], nums[l], nums[r])))
                    )
                    l += 1
                    r -= 1
                elif target < 0:
                    l += 1
                elif target > 0:
                    r -= 1

        return [x for x in result]


            