class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        origins = defaultdict(list)
        for fro, to, time in times:
            origins[fro].append((to, time))

        visited = set()
        min_heap = [(0, k)]
        ans = 0

        while min_heap:
            t1, v1 = heapq.heappop(min_heap)
            if v1 in visited:
                continue
            visited.add(v1)
            ans = max(ans, t1)
            
            for v2, t2 in origins[v1]:
                if v2 not in visited:
                    heapq.heappush(min_heap, (t1+t2, v2))


        return -1 if len(visited) < n else ans

# dfs(1, {}) = 4
# 1 + dfs(2, {1}) 
# 1 + dfs(3, {1,2})
# 1 + dfs(4, {1,2,3}) = 
# 1 + 0