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
            
            if len(path) == 0:
                start = 1
            else:
                start = path[-1]+1

            for j in range(start, n+1):
                path.append(j)
                bt(i+1)
                path.pop()

        bt(0)
        return result
