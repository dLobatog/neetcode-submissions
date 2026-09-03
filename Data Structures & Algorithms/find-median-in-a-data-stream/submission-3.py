from heapq import heappush_max, heappush, heappop, heappop_max

class MedianFinder:
    # keep 2 heaps
    # max heap of size k/2
    # min heap of size k/2
    # when you add
    # 1 - median is 1. add to minheap
    # 2 - median is 1.5, add to max heap since it's empty. median = min heap top / max_heap bottom / 2 
    # 3. - median is 2. is 3 > minheap? add to max heap

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap
        
    def addNum(self, num: int) -> None:
        if len(self.small) == 0 or num <= self.small[0]: # it's smaller than the "king" of the smalls. add it there
            heappush_max(self.small, num)
        else:
            heappush(self.large, num)

        # then maintain invariant - pop size until lengths differ by 1
        while len(self.small) - len(self.large) > 1:
            heappush(self.large, heappop_max(self.small))
        while len(self.large) - len(self.small) > 1:
            heappush_max(self.small, heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else: # same size
            return (self.large[0] + self.small[0]) / 2
         
        