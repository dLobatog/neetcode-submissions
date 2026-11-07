from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l, r = 0, 0
        results = []

        while r < len(nums):
            # evict old entries
            while q and q[0][1] <= r-k:
                q.popleft()

            entry = (nums[r], r)
            # pop every entry smaller than current
            while q and q[-1][0] < nums[r]:
                q.pop()

            # append entry
            q.append((nums[r], r))
            # print(q, r>= k-1, r)
            if r >= k-1:
                results.append(q[0][0])

            r += 1

        return results


