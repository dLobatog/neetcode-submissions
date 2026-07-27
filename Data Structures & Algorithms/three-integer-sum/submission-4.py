class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                target = -(nums[j] + nums[i]) # this would sum to 0
                # we need to make sure we're not using either i or j for target
                if target in seen:
                    result.append(tuple(sorted((nums[i], nums[j], target))))

                seen.add(nums[j])

        
        return [x for x in set(result)]