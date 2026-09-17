class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n + 1)

        def f(rem):
            if dp[rem] is not None:
                return dp[rem]
            if rem == 0:
                return 1

            ways = 0
            if rem - 1 >= 0:
                ways += f(rem - 1)
            if rem - 2 >= 0:
                ways += f(rem - 2)

            dp[rem] = ways
            return ways 

        return f(n)
