class Solution:
    def myPow(self, x: float, n: int) -> float:
        # we could split the n in 2 constantly?
        if x == 0:
            return 0.0
        elif x == 1:
            return 1.0
        elif x == -1:
            return 1.0 if n % 2 == 0 else -1.0
        elif n == 0:
            return 1.0
        elif n == -1:
            return 1/x
        elif n == 1:
            return x
        elif n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        elif n > 1:
            half = self.myPow(x, (n-1) // 2) 
            return half * half * x
        elif n < 1:
            half = self.myPow(x, (n+1) // 2) 
            return half * half * (1/x) 
