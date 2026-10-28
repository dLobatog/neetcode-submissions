class Solution:
    def reverseBits(self, n: int) -> int:
        result = [0] * 32
        i = 0
        while n > 0:
            result[i] = n % 2
            n //= 2
            i += 1

        final = 0
        exponent = 31
        for val in result:
            if val == 1:
                final += (2 ** exponent)
            exponent -= 1
        
        return final