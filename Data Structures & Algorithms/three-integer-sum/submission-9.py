class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # one option, make 2sum first with target 0
        #   - 2sum is O(n)
        # to find the 3rd number, iterate over 2sum solutions? 
        # other solution, sort, then do 2sum for sorted solution for each 
        # O(nlogn * n) - both are n**2

        def twosum(nums, target):
            comps = {}
            results = []
            for i, n in enumerate(nums):
                if n in comps:
                    results.append([nums[comps[n]], n])
                comps[target-n] = i
            return results 

        result = set()
        for i, n in enumerate(nums):
            candidates = twosum(nums[i+1:], -n)
            for c in candidates:
                result.add(tuple(sorted(c + [n])))
        
        return list(result)
            
            
        