class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) bc you must review the whole list
        dupes = defaultdict(int)
        for n in nums:
            dupes[n] += 1
            if dupes[n] >= 2:
                return n

        
