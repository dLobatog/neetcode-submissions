class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for n in nums:
            if n in res:
                return True
            res.add(n)

        return False
