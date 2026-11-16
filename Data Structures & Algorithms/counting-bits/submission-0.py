class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []
        for i in range(n+1):
            # 0 -> 0%2 == 0 - no bit
            # 1 -> 1%2 == 1 - bit?
            # 2 -> 2%2 == 0 - bit?
            bits = 0
            print(i)
            while i != 0:
                if i % 2 == 1:
                    bits += 1
                i //= 2
            results.append(bits)
    
        return results

