class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # operations to apply
        def op(a, b):
            return [max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2])]

        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i in range(3):
                if t[i] == target[i]:
                    good.add(i)

        for i in range(3):
            if i not in good:
                return False

        return True