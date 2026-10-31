class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep a heap of size k (o n log k?) and insert there -if full pop
        h = []
        count = Counter(nums)

        for n in count.keys():
            heapq.heappush(h, (count[n], n))
            if len(h) > k:
                heapq.heappop(h)

        return [n[1] for n in h]
