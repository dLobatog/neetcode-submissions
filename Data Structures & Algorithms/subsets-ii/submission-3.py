class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(i, cur):
            if i == len(nums):
                result.append(cur)
                return 

            helper(i+1, cur + [nums[i]])
            helper(i+1, cur)

        helper(0, [])

        resset = set()
        for subset in result:
            resset.add(tuple(sorted(subset)))

        return [x for x in resset] 