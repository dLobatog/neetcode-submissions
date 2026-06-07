class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_to_origin(x, y):
            return math.sqrt(((x-0)**2) + ((y-0)**2))

        h = []
        heapq.heapify(h)
        
        
        for x, y in points:
            heapq.heappush(h, (distance_to_origin(x, y), [x,y]))

        results = []
        while k:
            distance, point = heapq.heappop(h)
            results.append(point)
            k -= 1 

        return results


            