class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # [1,2,3,4,5,6]
        # it's been rotated a few times but remains in order
        # return true if target is in nums, false if not present
        # my plan:
        #.  1st: we find the pivot by doing binary search. 
        #        if at any point l > r - the pivot is between l and r. 
        #        when l < r - you have found the pivot - at mid? if mid+1 is > than mid and mid-1 < than mid
        #   2nd: using that, search in the part of the array that's necessary only
        # 
        # 3, 4, 4, 5, 6, 1, 2, 2 
        # findPivot(0,7) - mid = 7//2 = 3
        # nums[3] > nums[7]: 5 > 2, then l = 3, mid = 10//2 = 5
        # nums[5] > nums[7]: 1 < 2, then r = 5, mid = (10)//2=5
        # nums[5] = nums[5] - return 
        
        def findPivot(l, r):
            while l < r: 
                mid = (l + r)//2 
                # print(l, r, nums[mid], nums[r])
                if nums[mid] > nums[r]:
                    l = mid+1
                elif nums[mid] < nums[r]:
                    r = mid
                elif nums[mid] == nums[r]:
                    if nums[r-1] <= nums[r]:
                        r -=1
                    else:
                        # nums[r-1] > nums[r] ? then nums[r] is our pivot
                        return r
            return l

        def bs(l, r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] > target:
                    r = mid-1
                elif nums[mid] < target:
                    l = mid+1
                else:
                    return True
            
            return False


        
        pivot = findPivot(0, len(nums)-1) # consider pivot element 0 of array
        print('pivot', pivot)
        if nums[pivot] <= target <= nums[-1]:
            print('search pivot to end')
            return bs(pivot, len(nums)-1)
        else:
            print('search 0 to pivot')
            return bs(0, pivot-1)
    