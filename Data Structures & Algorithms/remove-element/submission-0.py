class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)
        # k = 0 # writer pointer
        # for i in range(len(nums)): # reader pointer
        #     if nums[i] != val:
        #         nums[k] = nums[i] 
        #         k += 1
            
        # return k 
