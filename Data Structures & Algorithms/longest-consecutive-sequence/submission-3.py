class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # each element is exactly "1" greater than the previous element
        # one way of doing this is, at each number, checking the rest:
        # n^2?
        #
        # 1 pass, save all numbers in a hash
        # 2nd pass, check if num + 1 exists
        # if num +1 doesn't exist - cannot start a sequence
        if len(nums) <= 1:
            return len(nums)
        target_nums = {}
        for num in nums:
            target_nums[num] = True
        
        valid_starts = []
        for num in nums:
            if (
                num+1 in target_nums and
                num-1 not in target_nums and
                num not in valid_starts
            ):
                valid_starts.append(num)

        if len(valid_starts) == 0:
            return 1
        
        result = 0
        for n in valid_starts:
            cur = n
            while cur+1 in target_nums:
                cur += 1
            result = max(1, cur - n + 1, result)
        
        return result

        