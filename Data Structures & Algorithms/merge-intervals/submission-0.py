class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        n = len(intervals)
        ans = [intervals[0]]
        i = 1

        while i < n:
            start, end = ans[-1]
            curr_start, curr_end = intervals[i]

            if curr_start > end:
                ans.append([curr_start, curr_end])
            else:
                start = min(start, curr_start)
                end = max(end, curr_end)
                ans[-1][0] = start
                ans[-1][1] = end

            i += 1

        return ans

        