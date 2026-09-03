from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        results = []
        dq = deque()
        
        for r in range(len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()

            dq.append(r)
            while dq and dq[0] < l:
                dq.popleft()
            
            if r >= k -1: # start recordin max
                results.append(nums[dq[0]])
                l += 1

        
        return results
            
            


            
