class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def helper(i, cur):
            if i == len(nums):
                result.append(cur)
                return 

            # take nums[i]
            helper(i+1, cur + [nums[i]])

            # since it's sorted, skip until different nums[i]?
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            helper(j, cur)

        helper(0, [])

        return result