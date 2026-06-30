class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 * 2 * 4 * 6
        # then, go over it again, dividing by each number
        # without division...
        # o(n) go over all numbers and multiply
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res  = [0] * n

        pref[0] = suff[n-1] = 1
        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]

        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res