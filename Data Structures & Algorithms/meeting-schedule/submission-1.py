"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda a: a.start)
        n = len(intervals)
        if n <= 0:
            return True

        start, end = intervals[0].start, intervals[0].end
        i = 1

        while i < n:
            curr_start = intervals[i].start
            curr_end = intervals[i].end

            if curr_start < end:
                return False

            start, end = curr_start, curr_end
            i += 1

        return True


