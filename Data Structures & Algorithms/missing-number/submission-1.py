class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        idealSet = set()
        for i in range(len(nums)+1):
            idealSet.add(i) 

        return list(idealSet - set(nums))[0]