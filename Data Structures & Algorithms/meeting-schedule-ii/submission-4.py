"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# room 0: 1, 5, (5, 9)
# room 1: 2, 6
# room 2: 3, 7
# room 3: 4, 8

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()

        res, count = 0, 0
        s, e = 0, 0


        while s < len(intervals):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            elif ends[e] <= starts[s]:
                count -= 1
                e += 1
            res = max(res,count)
        return res
