class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = set()
        for i, a in enumerate(nums):
            for j in range(i+1, len(nums)):
                b = nums[j]
                k, l = j + 1, len(nums)-1
                while k < l:
                    target_sum = a + b + nums[k] + nums[l]
                    if target_sum > target:
                        l -= 1
                    elif target_sum < target:
                        k += 1
                    else:
                        results.add((a, b, nums[k], nums[l]))
                        l -= 1
        return [list(c) for c in results]