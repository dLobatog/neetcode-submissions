class Solution:

    def sumOfSquares(self, n: int) -> int:
        total = 0
        for digit in str(n):
            total += int(digit)**2
        return total

    def isHappy(self, n: int) -> bool:
        # n = replace by sum of squares of its digets
        # repeate the above step until number = 1, or loops in a cycle that doesn't include 1 
        # if it stops at 1, return True, else False
        # how to know if cycle? check if n was seen before
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
            
        return True if fast == 1 else False
        
        return n == 1