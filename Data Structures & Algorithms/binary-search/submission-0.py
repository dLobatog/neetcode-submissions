class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(start, end):
            mid = (start + end) // 2

            if start > end:
                return -1

            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bsearch(start, mid-1) # branch left, as target would be left
            elif nums[mid] < target:
                return bsearch(mid+1, end) # branch right, as target would be right

        return bsearch(0, len(nums) - 1)