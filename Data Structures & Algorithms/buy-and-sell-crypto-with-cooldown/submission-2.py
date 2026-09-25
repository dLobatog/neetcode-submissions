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
        def f(i=0, origPrice=None):
            if i >= len(prices):
                return 0
            if origPrice in dp[i]:
                return dp[i][origPrice]

            buy = sell = hold = 0
            
            if origPrice == None:
                buy = f(i+1, prices[i]) # buy
            else:
                sell = (prices[i] - origPrice) + f(i+2, None)
            
            hold = 0 + f(i+1, origPrice)

            profit = max(buy, sell, hold)
            dp[i][origPrice] = profit
            return profit

        dp = [defaultdict(int) for _ in range(len(prices)+1)]

        return f()