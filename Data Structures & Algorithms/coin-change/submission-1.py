class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # fewest coin you need to make that exact amount
        # at position 1, you need to divide amount / coins[0]
        # then, what if you did the same on position 1
        # amount / coins[1] + amount % coins[1] (divide this by coins[0])
        # why not do this greedily
        # you're guaranteed that using the highest possible coin is always gonna result in less coins
        # amount=10, [5,9] - greedy won't work bc you can't take 9 then 5
        # coins[0] min amount of coins = amount / coins and amount % coins  == 0
        # think in terms of recursion
        # we can choose to pick 1 or not
        # we can choose to pick 5 or not
        # we can choose to pick 10 or not
        #f(remaining) = minimum number of additional coins
        #      needed to make exactly this remaining amount.

        # f(0) = 0
        # f(i) = 1 + f(i - c) for c in coins
        dp = [None] * (amount + 1)

        def f(r):
            if dp[r] is not None:
                return dp[r]
            if r == 0:
                return 0
            
            best = float('inf')
            for c in coins:
                if r - c >= 0:
                    best = min(best, 1 + f(r - c))

            dp[r] = best
            return best

        best = f(amount)
        if best == float('inf'):
            return -1

        return best

        