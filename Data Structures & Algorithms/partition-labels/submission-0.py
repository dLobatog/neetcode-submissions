class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}

        for i, c in enumerate(s):
            if c not in intervals:
                intervals[c] = [i, i]
            else:
                intervals[c][-1] = i # update the end

        # then merge intervals? and count size of merged intervals?
        ints = []
        for k, v in intervals.items():
            ints.append(v)

        ints.sort()
        if len(ints) == 1:
            return [ints[0][1] - ints[0][0] + 1]

        cur = ints[0]
        results = []
        for i in range(1, len(ints)):
            start, end = ints[i]
            if cur[1] >= start:
                # merge
                cur[1] = max(end, cur[1])
            else:
                # new interval
                results.append(cur[1]-cur[0]+1)
                cur = [start, end]

        results.append(cur[1]-cur[0]+1)
        return results




