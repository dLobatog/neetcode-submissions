class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # in a set keep uniques
        k = 1

        # i=reader
        # k=writer
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k


