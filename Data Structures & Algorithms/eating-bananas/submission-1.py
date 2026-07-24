class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search for k is my initial thought
        # h is the total amount of hours 
        # [1, 2, 3, 4] - take mid number (4/2) - try if possible
        # # how to try in O(n)? iterate array, removing - k bananas per hour

        def can_finish(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k) # pile / k how many hours to finish this pile
            return hours <= h
            
        left, right = 1, max(piles)
        res = right 
        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                # try a smaller k
                res = mid 
                right = mid - 1
            else:
                left = mid + 1

        return res

                