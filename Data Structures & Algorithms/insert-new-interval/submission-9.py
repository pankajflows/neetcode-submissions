class Solution:
    def insert22(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        g = newInterval
        i = 0
        while i < len(intervals)-1:
            a = intervals[i]
            b = intervals[i+1]
            print(i)
            print(a, b)
            print("  ", g)
            if a[1] < g[0] and g[1] < b[0]:
                print("case1")
                intervals.insert(i+1, g)
                break
            elif g[0] <= a[1] and g[0] >= a[0] and g[1] < b[0]:
                print("case2")
                a[1] = g[1]
                break
            elif a[1] < g[0] and g[1] >= b[0] and g[1] <= b[1]:
                print("case3")
                b[0] = g[0]
                break
            elif g[0] <= a[1] and g[1] >= b[0]:
                print("case4")
                a[1] = max(b[1], g[1])
                intervals.pop(i+1)
                p = i
                q = i+1
                while q < len(nums):
                    a = nums[p]
                    b = nums[q]
                        
                    p += 1
                    q += 1

                

            i += 1

        return intervals


    def insert33(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) < 1:
            return [newInterval]
        ans = list()
        start, end = newInterval
        ip = None

        # Finding the insertion point
        for i in range(len(intervals)):
            curr = intervals[i]
            if start > curr[1]:
                ans.append(curr)
            else:
                print("found insertion point", i)
                ip = i
                break
        j = ip
        backfill = False

        # merge
        if end < intervals[ip][0]:
            print("safe to append, no merge required")
            ans.append([start, end])
            ans.append(intervals[ip])
            j += 1
        else:
            print("merge required at", ip)
            mstart = min(intervals[ip][0], start)
            mend = max(intervals[ip][1], end)
            print("merge started interval", mstart, mend)
            # Merging till possible
            for i in range(ip+1, len(intervals)):
                j = i
                curr = intervals[i]
                if curr[0] > mend:
                    backfill = True
                    break
                mstart = min(mstart, curr[0])
                mend = max(mend, curr[1])
            print("merge ended interval", mstart, mend)
            ans.append([mstart, mend])
        

        # Appending the rest of it
        if backfill:
            for i in range(j, len(intervals)):
                print("Appending the rest", i)
                ans.append(intervals[i])

        return ans


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = list()
        n = len(intervals)
        mstart, mend = newInterval
        i = 0
        while i < n and intervals[i][1] < mstart:
            ans.append(intervals[i])
            i += 1

        while i < n and mend >= intervals[i][0]:
            mstart = min(intervals[i][0], mstart)
            mend = max(intervals[i][1], mend)
            i += 1
        ans.append([mstart, mend])

        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans


















