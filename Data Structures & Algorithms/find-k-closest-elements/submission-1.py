class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find closest to x. 
        h = []
        for i, n in enumerate(arr):
            if len(h) < k:
                heapq.heappush(h, n)
                continue
            
            val = heapq.heappop(h) # at k elements, pop
            if abs(val-x) > abs(n-x):
                heapq.heappush(h, n)
            else:
                heapq.heappush(h, val)
        results = []
        while h:
            results.append(heapq.heappop(h))
        return results