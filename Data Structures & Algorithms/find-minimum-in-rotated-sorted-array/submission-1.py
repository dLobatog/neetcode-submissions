class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while start != end:
            midIndex = (start + end)//2
            if nums[midIndex] < nums[end]: # right side is sorted, look left
                end = midIndex # midIndex - 1 
            elif nums[midIndex] > nums[end]:  
                start = midIndex + 1

        return nums[start]