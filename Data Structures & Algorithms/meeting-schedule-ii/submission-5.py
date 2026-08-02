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
        time = []
        for i in intervals:
            time.append((i.start, +1))
            time.append((i.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        res, count = 0, 0
        for event, startOrEnd in time:
            count += startOrEnd
            res = max(count, res)
        return res