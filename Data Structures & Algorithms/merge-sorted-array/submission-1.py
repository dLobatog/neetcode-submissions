class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [2,3,4,0,0]
        # [1,5]
        # i,j,w = = 2,1,4 - [2,3,4,0,0]
        #   - 2 is greater, 
        # i,j,w = 2,0,3 [2,3,4,0,5]
        #   - 1 is greater
        # i,j,w = 1,0,2 [2,3,4,4,5]
        #   - 3>1, 3 is greater 
        # i,j,w = 0,0,1 [2,3,3,4,5]
        #.  - 2>1, 2 is greater
        # i,j,w = -1,0,0 [2,2,3,4,5]
        #.  - 1>none?, 1 is greater
        # i,j,w = -1,-1,-1 [1,2,3,4,5]
        
        i, j, w = m-1, n-1, m + n -1
        while i>=0 and j >= 0 and w >= 0:
            if i>=0 and j>=0 and nums2[j] > nums1[i]:
                nums1[w] = nums2[j]
                j -= 1
            else:
                nums1[w] = nums1[i]
                i -= 1

            w -= 1 

        while w >= 0:
            if i >= 0:
                nums1[w] = nums1[i]
                i -= 1
            elif j >= 0:
                nums1[w] = nums2[j]
                j -= 1
            w -= 1 

