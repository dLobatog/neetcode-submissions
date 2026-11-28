from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]: # we have profit so save it
                profit += (prices[i]-prices[i-1])
            
        return profit
