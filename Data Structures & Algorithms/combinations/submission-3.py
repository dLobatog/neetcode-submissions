class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # at each position (range k)
        # you may choose a number from 1 to n
        # open a new branch for each number
        result = []
        path = []

        def bt(i):
            if i == k:
                result.append(path.copy())
                return
            
            for j in range(1, n+1):
                if len(path) == 0 or j > path[-1]:
                    path.append(j)
                    bt(i+1)
                    path.pop()

        bt(0)
        return result
