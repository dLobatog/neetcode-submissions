class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1,2,3,4,5,6]
        # [3,4,5,6,1,2]
        # [6,1,2,3,4,5]

        # find the pivot (in log(n)) time
        # if target > pivot - look in nums[pivot:]
        # else nlooks in nums[:pivot]

        # to look for the pivot
        # look left and right until you find a point where 
        # nums[mid] > nums[mid+1] or nums[mid] < nums[mid-1]
        def findPivot(l, r) -> int:
            if l == r:
                return l 
            if l > r:
                return -1
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                # this part is sorted, so the smallest elmeent must be on the left
                return findPivot(l, mid)
            
            # nums[mid] should've been smaller if it was sorted... look right
            return findPivot(mid+1, r)
            
        pivot = findPivot(0, len(nums)-1) 
        # pivot is the smallest element
        l, r = 0, len(nums)-1
    
        if target >= nums[pivot] and target <= nums[-1]: 
            l, r = pivot, len(nums)-1
        else:
            l, r = 0, pivot-1
        print(pivot, l , r)
    
        # print(pivot, l , r)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else: # nums[mid] < target
                l = mid+1

        return -1
        

