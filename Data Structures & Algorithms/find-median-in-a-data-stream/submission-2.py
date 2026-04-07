from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small = [] # max-heap - so add with -1 * 
        self.large = [] # min-heap

    def addNum(self, num: int) -> None:
        # always push to small first
        heappush(self.small, -num)
        # make sure every element in small is <= every element in large
        heappush(self.large, -heappop(self.small))

        # rebalance if large is too big
        if len(self.large) - len(self.small) > 1:
            heappush(self.small, -heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        
        left, right = self.large[0], -1 * self.small[0]
        return (left + right) / 2
