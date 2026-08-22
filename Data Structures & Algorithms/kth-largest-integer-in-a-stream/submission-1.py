class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        heapq.heapify(self.h)
        for n in nums:
            heapq.heappush(self.h, n)
            if len(self.h) > k:
                heapq.heappop(self.h)
        
        # push k numbers
        # when you pop, you will pop the smallest. discard it and keep pushing 
        

    def add(self, val: int) -> int:
        # check the top of the heap. pop until value popped < val, then push val
        # while self.h[]
        # print("before val", val, self.h)
        while self.h and len(self.h) >= self.k and self.h[0] < val:
            heapq.heappop(self.h)
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        # print("after val", val, self.h)
        return self.h[0]


# [2,3,3] - 3
# [3,3,5] - 3
# [3,3,3]
