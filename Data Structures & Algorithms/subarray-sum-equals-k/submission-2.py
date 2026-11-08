class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0 
        running = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        for n in nums:
            running += n

            if running-k in prefix_counts:
                result += prefix_counts[running-k]

            prefix_counts[running] += 1

        return result