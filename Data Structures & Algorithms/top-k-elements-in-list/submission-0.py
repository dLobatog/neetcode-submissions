class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most frequent elements within the array
        # if k = 2 - return 3 and 2 
        # keep counts for each element in a good datastructure
        # heap for counts (count, element) ? 

        h = []
        heapq.heapify(h)
        count = defaultdict(int)
        # heappush(h, (count, element))
        for n in nums:
            count[n] += 1
            heapq.heappush(h, (-count[n], n))

        result = set()
        while k > 0:
            count, element = heapq.heappop(h)
            # print(element, count)
            if element not in result:
                result.add(element)
                k -= 1
        return list(result)

