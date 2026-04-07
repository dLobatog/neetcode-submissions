class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def pickUntilTarget(i, chosenNums):
            nonlocal combinations, target, nums

            totalSum = sum(chosenNums)

            if totalSum == target:
                combinations.append(list(chosenNums))
                return

            if i >= len(nums) or totalSum > target:
                return
            
            # at every index, we can either pick it or not pick it. 
            # we pick it if sum + nums[i] <= remaining
            
            chosenNums.append(nums[i])
            pickUntilTarget(i, chosenNums)
            chosenNums.pop()
            pickUntilTarget(i+1, chosenNums)
                

        pickUntilTarget(0, [])
        return combinations
