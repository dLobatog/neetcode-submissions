class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # separates the lower half from the upper half
        # condition = find an index i s.t
        # left1[i] <= right2[i+1] 
        # left2[i] <= right1[i+1]
        search_a, bigger_a = nums1, nums2
        if len(nums1) >= len(nums2):
            search_a, bigger_a = nums2, nums1
        

        total = len(nums1) + len(nums2)
        half = total // 2 # that's how much you want on either side

        l, r = 0, len(search_a) 

        while l <= r:
            mid = (l + r)//2
            bigger_mid = half - mid

            L1 = float("-inf") if mid == 0 else search_a[mid - 1]
            L2 = float("-inf") if bigger_mid == 0 else bigger_a[bigger_mid - 1]
            R1 = float("inf") if mid == len(search_a) else search_a[mid]
            R2 = float("inf") if bigger_mid == len(bigger_a) else bigger_a[bigger_mid]
            if L1 <= R2 and L2 <= R1:
                if total % 2:
                    return min(R1, R2)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2
            elif L1 > R2:
                # cut pequeño demasiado a la derecha
                r = mid - 1
            elif L2 > R1:
                l = mid + 1
        
        
