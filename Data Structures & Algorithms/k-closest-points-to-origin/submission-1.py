class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_to_origin(x, y):
            return math.sqrt(((x-0)**2) + ((y-0)**2))

        h = []
        heapq.heapify(h)
        
        
        for x, y in points:
            heapq.heappush(h, (-distance_to_origin(x, y), [x,y]))
            if len(h) > k:
                heapq.heappop(h)

        return [point for (dist, point) in h]
        