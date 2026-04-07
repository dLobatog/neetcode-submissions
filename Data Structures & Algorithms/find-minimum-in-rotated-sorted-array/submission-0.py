class Solution:
    def findMin(self, nums: List[int]) -> int:

        def bsearch(nums: List[int], start, end) -> int:
            if start == end:
                return nums[start]
            
            midIndex = (start + end)//2
            
            if nums[midIndex] > nums[end]:
                return bsearch(nums, midIndex + 1, end)
            else:
                return bsearch(nums, start, midIndex)
            

        return bsearch(nums, 0, len(nums) - 1)