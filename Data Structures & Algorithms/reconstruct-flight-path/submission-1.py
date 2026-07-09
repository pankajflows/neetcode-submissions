class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for fro, to in tickets:
            heapq.heappush(adj[fro], to)

        ans = []

        def dfs(curr):
            while adj[curr]:
                next = heapq.heappop(adj[curr])
                dfs(next)
            ans.append(curr)

        dfs("JFK")
        return ans[::-1]





        