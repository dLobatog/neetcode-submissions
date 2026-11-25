class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            mid = (l+r)//2
            pw = mid * mid
            if pw < x:
                l = mid+1
                res = mid
            elif pw > x:
                r = mid-1
            else:
                return mid

        return res