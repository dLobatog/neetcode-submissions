class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most frequent elements within the array
        # if k = 2 - return 3 and 2 
        # keep counts for each element in a good datastructure
        # heap for counts (count, element) ? 

        count = defaultdict(int)
        # heappush(h, (count, element))
        for n in nums:
            count[n] += 1
        
        h = []
        heapq.heapify(h)
        for num, freq in count.items():
            heapq.heappush(h, (freq, num))
            if len(h) > k:
                heapq.heappop(h)


        result = []
        while k > 0:
            count, element = heapq.heappop(h)
            if element not in result:
                result.append(element)
                k -= 1
        return result

