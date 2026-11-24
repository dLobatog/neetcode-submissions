# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        mid = (l+r)//2
        while l <= r:
            mid = (l+r)//2
            g = guess(mid)
            if g == -1: # guess is higher than number, must look left
                r = mid-1
            elif g == 1: # guess is smaller, so i must look right
                l = mid+1
            else:
                return mid

        return mid