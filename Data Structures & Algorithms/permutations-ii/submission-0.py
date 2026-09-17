class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        counts = Counter(nums)
        path = []

        def bt(i):
            if i == len(nums):
                results.append(path.copy())
                return

            for key, val in counts.items():
                if val != 0:
                    counts[key] -= 1
                    path.append(key)
                    bt(i+1)
                    path.pop()
                    counts[key] += 1

        bt(0)
        return results

        