class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        group = []

        def backtrack(i, remainder):
            if remainder == 0:
                result.append(group.copy())
                return 

            if i >= len(candidates) or remainder < candidates[i]:
                return 

            group.append(candidates[i])
            backtrack(i+1, remainder-candidates[i])
            group.pop()
            
            value = candidates[i]
            while i < len(candidates) and candidates[i] == value:
                i += 1

            backtrack(i, remainder)

        backtrack(0, target)
        return result

            
