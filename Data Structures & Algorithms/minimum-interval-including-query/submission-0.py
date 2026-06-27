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

        for sq in sorted_queries:
            query, query_index = sq
            heap = list()
            for left, right in intervals:
                if left <= query:
                    heapq.heappush(heap, (right-left+1, left, right, query_index))

            while heap:
                smallest_gap, left, right, query_index = heapq.heappop(heap)
                if query <= right:
                    ans[query_index] = smallest_gap
                    break

        return ans



        