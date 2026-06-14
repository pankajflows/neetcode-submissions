"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms2(self, intervals: List[Interval]) -> int:
        # naive approach
        intervals.sort(key=lambda a: a.start)
        n = len(intervals)
        if n <= 0:
            return 0
        ans = 1
        start, end = intervals[0].start, intervals[0].end
        i = 1

        while i < n:
            curr_start = intervals[i].start
            curr_end = intervals[i].end

            if curr_start < end:
                ans += 1

            start, end = curr_start, curr_end
            i += 1

        return ans


    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key=lambda a: a.start)
        if len(intervals) == 1:
            return 1
        starts = list()
        ends = list()
        n = len(intervals)
        ans = count = 0
        for inter in intervals:
            starts.append(inter.start)
            ends.append(inter.end)
        starts.sort()
        ends.sort()
        s = 0
        e = 0

        while s < n and e < n:
            if  s < n and starts[s] < ends[e]:
                s += 1
                count += 1
            else:  
                e += 1
                count -= 1

            ans = max(ans, count)

        return ans












