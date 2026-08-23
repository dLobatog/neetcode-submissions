class Solution:
    def isHappy(self, n: int) -> bool:
        # n = replace by sum of squares of its digets
        # repeate the above step until number = 1, or loops in a cycle that doesn't include 1 
        # if it stops at 1, return True, else False
        # how to know if cycle? check if n was seen before
        seen = set()

        while n != 1:
            if n in seen:
                break
            if n not in seen:
                seen.add(n)
            total = 0
            for digit in str(n):
                total += int(digit)**2
            
            n = total
        
        return n == 1