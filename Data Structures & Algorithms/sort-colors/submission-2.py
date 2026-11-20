from random import randint

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # quicksort
        # pick random pivot
        # anything < random pivot goes to one array
        # anything > random pivot goes to another array
        # pivot = nums[randint(0, len(nums)-1)]
        l, r = 0, len(nums)-1
        i = 0
        
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:            
                i += 1