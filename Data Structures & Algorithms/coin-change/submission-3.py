class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # My function returns exactly: ______.
        # Its arguments contain everything needed because: ______.
        # My choices are: using one coin, recurse on amount.
        # I combine their answers using: ______.
        #Finishing successfully returns: fewest # of coins to make amount.
        #An impossible situation returns: -1.
        dp = [None] * (amount + 1)

        def f(rem):
            if dp[rem] is not None:
                return dp[rem]
            if rem == 0:
                return 0

            best = float('inf')
            for c in coins:
                if rem - c >= 0:
                    best = min(1 + f(rem-c), best)

            dp[rem] = best
            return best

        result = f(amount)

        if result == float('inf'):
            return -1
        else:
            return result
