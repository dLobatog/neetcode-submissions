class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # at every index you can either add or not, and move on
        # recursively
        results = {}
        def helper(i, subset):
            if tuple(subset) not in results:
                results[tuple(subset)] = 0
            if i >= len(nums):
                return
            new_subset = subset + [nums[i]]
            helper(i + 1, new_subset)
            helper(i + 1, subset)

        helper(0, [])

        return [list(k) for k in results.keys()]
            
        
            
        