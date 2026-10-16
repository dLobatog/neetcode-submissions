class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in seen:
                for j in seen[nums[i]]:
                    if abs(j-i) <= k:
                        return True

            seen[nums[i]].append(i)

        return False