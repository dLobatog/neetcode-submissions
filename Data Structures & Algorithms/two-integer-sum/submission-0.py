class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {} # saves "complement": index
        # 3,4,5,6, target 7
        # i - n
        # 0.  3. 7-3=4 {4:0}
        # 1.  4. is 3 in there? no {4:0, }
        for i, n in enumerate(nums):
            # print(i, n)
            if n in complements:
                return [complements[n], i]
            complements[target-n] = i
        return []