class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the minimum number index. then recompose array
        # once array is reocmposed, binary search. O(n)
        
        def bsearch(i, j):
            if i > j or i < 0 or j >= len(nums):
                return -1 

            mid = (j + i) // 2
            print(i, j, mid, nums[mid])

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # then the target must be on the right... unless it's rotated
                # look first on the right 
                result_index = bsearch(mid+1, j)
                # if not, look on the left
                if result_index != -1:
                    return result_index

                second_try = bsearch(i, mid-1)
                if second_try != -1:
                    return second_try
                return -1
            elif nums[mid] > target:
                # then the target must be on the left... unless it's rotated
                result_index = bsearch(i, mid-1)
                # if not, look on the left
                if result_index != -1:
                    return result_index
                
                second_try = bsearch(mid+1, j)
                if second_try != -1:
                    return second_try
                return -1

        return bsearch(0, len(nums)-1)