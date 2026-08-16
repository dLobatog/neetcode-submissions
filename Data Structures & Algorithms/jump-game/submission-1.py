class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max jump at each position  
        dps = [None] * len(nums)
        def dp(i):
            # print(i, nums[i])
            if dps[i] is not None:
                return dps[i]

            if i == len(nums)-1:
                return True

            if nums[i] == 0:
                return False

            for j in range(1, nums[i]+1): # explore jumps
                # print(j, nums[j])
                possible_end = dp(i + j)
                if possible_end:
                    dps[i+j] = True
                    return True

            dps[i] = False
            return False

        return dp(0)
        