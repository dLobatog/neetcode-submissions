class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # since majority element appears > half of the time
        # if we keep a counter, increasing with the number
        # decreasing when different 
        # the candidate will always prevail as it has > 1/2 of the array
        candidate = None
        count = 0

        for n in nums:
            if count == 0:
                candidate = n

            if n != candidate:
                count -= 1
            else:
                count += 1

        return candidate