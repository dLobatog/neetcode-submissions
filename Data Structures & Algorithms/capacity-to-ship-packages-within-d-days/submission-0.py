class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def simulate(capacity):
            load, days = 0, 1
            for w in weights:
                if load + w > capacity:
                    days += 1
                    load = w
                else:
                    load += w

            return days


        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            daysToLoad = simulate(mid)
            if daysToLoad > days:
                # increase capacity to load faster
                l = mid+1
            else:
                # reduce capacity to load slower
                r = mid

        return l
