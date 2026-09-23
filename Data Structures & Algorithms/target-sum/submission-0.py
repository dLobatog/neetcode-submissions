from functools import cache
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def f(i, temp):
            if i == len(nums):
                return int(temp == target)

            return (
                f(i + 1, temp - nums[i])
                + f(i + 1, temp + nums[i])
            )

        return f(0, 0)