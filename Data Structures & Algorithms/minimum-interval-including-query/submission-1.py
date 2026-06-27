class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import bisect
        ans = list()

        # sort based on first index
        intervals.sort(key=lambda a: a[0])

        sorted_queries = list()
        for i in range(len(queries)):
            sorted_queries.append((queries[i], i))
        sorted_queries.sort(key=lambda x: x[0])

        ans = [-1]*len(queries)
        heap = list()
        i = 0

        for sq in sorted_queries:
            query, query_index = sq
            while i < len(intervals) and intervals[i][0] <= query:
                left = intervals[i][0]
                right = intervals[i][1]
                heapq.heappush(heap, (right-left+1, left, right, query_index))
                i += 1

            while heap and query > heap[0][2]:
                heapq.heappop(heap)
            
            if heap:
                ans[query_index] = heap[0][0]

        return ans



        