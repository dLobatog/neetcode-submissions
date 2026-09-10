class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            next_prices = prices.copy()

            for u, v, price in flights:
                if prices[u] != float("inf"):
                    next_prices[v] = min(
                        next_prices[v],
                        prices[u] + price
                    )

            prices = next_prices

        if prices[dst] == float('inf'):
            return -1

        return prices[dst]







