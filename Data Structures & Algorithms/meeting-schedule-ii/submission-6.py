"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # minimum meeting rooms = max number of conflicts?
        events = []

        for interval in intervals:
            start, end = interval.start, interval.end
            events.append((start, +1))
            events.append((end,   -1))

        events.sort()
        max_concurrent = 0 
        current = 0

        for timestamp, tick in events:
            current += tick
            max_concurrent = max(max_concurrent, current)

        return max_concurrent

        