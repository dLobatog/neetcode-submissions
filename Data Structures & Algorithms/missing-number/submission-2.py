class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor all numbers together from 0 to n
        # then iterate through array
        # missing number would be that

        result = 0
        for i in range(len(nums)+1):
            result ^= i
            
        for n in nums:
            result ^= n

        return result