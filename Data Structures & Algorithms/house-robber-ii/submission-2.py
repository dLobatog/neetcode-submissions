class Solution:
    def rob(self, nums: List[int]) -> int:
        # you can rob at nums[i]
        # if you rob at nums[i] 
        #.    -you should rob next at nums[i+1] at most
        #     -you must not have robbed at nums[i-1]
        # find out how much can you rob
        # def dp(i, acc):
        #     if i >= len(nums):
        #         return acc

        #     jumpTwo = dp(i+2, acc+nums[i]) 
        #     jumpOne = dp(i+1, acc)
        #     return max(jumpOne, jumpTwo)
        # if homes are on a circle, max at 0 is either max(0 or max(0, -1))
        # what about 2 runs on nums[1:] and nums[:-1]
        # [9,8,3,6] = 15
        # [2,9,8,3] = 12
        # max= 12

        def houserob(nums):
            if len(nums) <= 2:
                return max(nums)

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(
                    dp[i-2] + nums[i],
                    dp[i-1]
                )

            # print(dp)

            return dp[-1]

        if len(nums) <= 2:
            return max(nums)

        # print(nums[1:])
        # print(nums[:-1])
        return max(houserob(nums[1:]), houserob(nums[:-1]))

        # return dp(0, 0)