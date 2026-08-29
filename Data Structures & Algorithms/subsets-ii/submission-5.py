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
            numtoskip = nums[i]
            while i < len(nums) and nums[i] == numtoskip:
                i += 1 
            helper(i, cur)

        helper(0, [])

        return result