class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # choose a single day to buy, a single day to sell
        # if sequence is decreasing, don't sell (0)
        # highest increasing subsequence
        # if at some point, it increases, then sell (0) or don't sell

        if len(prices) < 2:
            return 0
        
        maxProfit = 0
        lowestSoFar = prices[0]

        for price in prices[1:]:
            if price < lowestSoFar:
                lowestSoFar = price
            
            maxProfit = max(price - lowestSoFar, maxProfit)
        
        return maxProfit