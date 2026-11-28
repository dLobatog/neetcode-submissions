class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums)/3
        count = {}
        res = set()
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            
            if count[n] > target:
                res.add(n)


        return list(res)