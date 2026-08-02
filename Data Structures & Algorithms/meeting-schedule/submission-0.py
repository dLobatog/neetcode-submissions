"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # just need to determine conflicts
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda x: x.start)
        prevEnd = intervals[0].end
        for interval in intervals[1:]:
            newStart, newEnd = interval.start, interval.end
            if prevEnd > newStart:
                return False
            
            prevEnd = newEnd
        return True

