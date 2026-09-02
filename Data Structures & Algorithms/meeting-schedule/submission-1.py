"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # calculate concurrent events, if no concurrent, then we're good. 
        events = []

        for interval in intervals:
            start, end = interval.start, interval.end
            events.append((start, +1))
            events.append((end, -1))

        events.sort()
        concurrent = 0
        for time, tick in events:
            concurrent += tick
            if concurrent > 1:
                return False

        return True
