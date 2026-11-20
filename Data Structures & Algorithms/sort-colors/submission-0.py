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
        pivot = 1
        lt = []
        gt = []
        eq = []
        for n in nums:
            if n < pivot:
                lt.append(n)
            elif n > pivot:
                gt.append(n)
            else:
                eq.append(n)

        result = lt + eq + gt
        for i in range(len(nums)):
            nums[i] = result[i]



