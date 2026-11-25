class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            m = nums[mid]
            if m == target: 
                return mid
            elif m < target:
                l = mid+1
            else:
                r = mid-1

        # if not found, we'll be at l=r
        if nums[l] < target:
            return l+1
        elif nums[l] > target:
            return l 
        else:
            return l


