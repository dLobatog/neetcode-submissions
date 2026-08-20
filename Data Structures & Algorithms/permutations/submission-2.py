class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        # take all permutations for all numbers except the first
        perms = self.permute(nums[1:])
        # then put nums[0] in all possible positions
        res = []
        for p in perms: # 
            for i in range(len(p) + 1): # you can and at the end of the permutation
                copy_p = p.copy()
                copy_p.insert(i, nums[0])
                res.append(copy_p)

        return res

