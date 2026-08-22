class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]

        h = []
        heapq.heapify_max(h)
        for s in stones:
            heapq.heappush_max(h, s)

        # print(h)
        x = heapq.heappop_max(h)
        y = heapq.heappop_max(h)
        
        new_stones = []
        for s in h:
            new_stones.append(s)

        if x > y:
            new_stones.append(x - y)
        elif x < y:
            new_stones.append(y - x)
        # else do nothing don't append either stone
        # print(x, y, new_stones)
        return self.lastStoneWeight(new_stones)