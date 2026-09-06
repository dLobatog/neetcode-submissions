class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        ordered_queries = sorted(
            (q, idx) for idx, q in enumerate(queries)
        )
        heap = [] 
        result = [-1] * (len(queries))
        START, END = 0, 1
        i, j = 0, 0 
    
        while i < len(queries):
            query, original_idx = ordered_queries[i]

            # push to heap (len, end)
            while j < len(intervals) and intervals[j][START] <= query:
                heapq.heappush(
                    heap, 
                    (
                        intervals[j][END] - intervals[j][START] + 1, 
                        intervals[j][END]
                    )
                )
                j += 1

            # pop from heap unusable values
            while heap and heap[0][END] < query:
                heapq.heappop(heap)

            if heap:
                result[original_idx] = heap[0][0]

            i += 1


        return result

