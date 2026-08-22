class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # a heap would allow us to keep k elements sorted
        # we make sure to insert up to k elements (first)
        # then, never insert an element smaller than heap[0] 
        #.   (you'd be breaking the invariant) that the heap stores kth largest element
        #. if an element > heap[0] is found, pop and push
        #  return that element
        h = []
        heapq.heapify(h)
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
                continue
            
            if n > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, n)

        return h[0]

