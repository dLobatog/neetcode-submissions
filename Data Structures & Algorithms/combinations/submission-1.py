class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # at each position (range k)
        # you may choose a number from 1 to n
        # open a new branch for each number
        result = set()
        path = []

        def bt(i):
            if i == k:
                result.add(tuple(path))
                return
            
            for j in range(1, n+1):
                if j not in path and (len(path) == 0 or j > path[-1]):
                    path.append(j)
                    bt(i+1)
                    path.pop()

        bt(0)
        return [list(x) for x in result]
