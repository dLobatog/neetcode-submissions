class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor every number with each other? 
        result = 0 
        for num in range(0, len(nums)+1):
            result ^= num

        for num in nums:
            result ^= num
        
        return result
        
        