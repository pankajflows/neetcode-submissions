class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a: a[0])
        n = len(intervals)
        ans = 0

        i = 0
        j = 1

        while j < n:
            s1, e1 = intervals[i]
            s2, e2 = intervals[j]

            if s2 < e1:
                ans += 1
                if e1 > e2:
                    i = j
            else:
                i = j

            j += 1

        return ans

        