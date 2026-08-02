class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # sort by start
        res = 0
        prevEnd = intervals[0][1]
        for startNew, endNew in intervals[1:]:
            if startNew >= prevEnd: # no overlap
                prevEnd = endNew
            else:
                res += 1 # there's an overlap, so we must delete
                prevEnd = min(prevEnd, endNew)

        return res

