from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small = [] # max-heap   - so add with -1
        self.large = [] # min-heap

    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -1 * num)

        # rebalance
        if len(self.large) - len(self.small) > 1:
            element = heappop(self.large)
            heapq.heappush(self.small, -1 * element)
        elif len(self.small) - len(self.large) > 1:
            element = heappop(self.small)
            heappush(self.large, -1 * element)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # get max 
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            element1, element2 = self.large[0], -1 * self.small[0]
            return (element1 + element2) / 2


        return 0.0


        
        