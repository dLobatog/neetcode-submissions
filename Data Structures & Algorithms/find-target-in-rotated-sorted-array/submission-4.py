class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the minimum number index. then recompose array
        # once array is reocmposed, binary search. O(n)
        
        def bsearch_smallest(left, right):
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    # Pivot must be to the right of mid
                    left = mid + 1
                else:
                    # Mid might itself be the pivot
                    right = mid

            return left

        pivot = bsearch_smallest(0, len(nums)-1)
        
        if nums[pivot] <= target <= nums[-1]: # search the right 
            l, r = pivot, len(nums)-1
        # elif target < nums[pivot] and target >= nums[0]: # search the left
        else:
            l, r = 0, pivot

        mid = (l + r)//2
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > target:
                # search left
                r = mid-1
            elif nums[mid] < target:
                # search right
                l = mid+1
            else:
                return mid
            
        return -1