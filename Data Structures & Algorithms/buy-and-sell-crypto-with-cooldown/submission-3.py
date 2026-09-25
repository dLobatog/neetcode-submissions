class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i]
        # if you buy, you can't buy the next day
        # you must by i+2 then
        # you can only own one neetcoin at a time
        # initial thoughts
        # 
        #. options:
        #.    - buy and jump to i+1
        #.    - sell and jump to i+2
        #.    - hold and jump to i+1
        #. max profit is the max returned from all those
        #. state to carry: price of the original coin
        def f(i=0, canBuy=True):
            if i >= len(prices):
                return 0
            if dp[i][canBuy] is not None:
                return dp[i][canBuy]

            buy = sell = hold = 0
            
            if canBuy == True:
                buy = f(i+1, False) - prices[i]
            else:
                sell = f(i+2, True) + prices[i]
            
            hold = 0 + f(i+1, canBuy)

            profit = max(buy, sell, hold)
            dp[i][canBuy] = profit
            return profit

        dp = [[None for _ in range(2)] for _ in range(len(prices)+1)]

        return f()