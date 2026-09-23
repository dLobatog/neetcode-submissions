class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # coins [1,5,10,etc..]
        # amount 300
        # - from a tree perspective
        # amount -= coin[i] 
        # if amount == 0 - found a result
        dp = [[None for _ in range(amount+1)] for _ in range(len(coins))]

        def f(i, remaining):
            if dp[i][remaining] is not None:
                return dp[i][remaining]
            if remaining < 0:
                return 0
            if remaining == 0:
                return 1

            ways = 0
            for j in range(i, len(coins)):
                ways += f(j, remaining-coins[j])

            dp[i][remaining] = ways
            return ways

        return f(0, amount)