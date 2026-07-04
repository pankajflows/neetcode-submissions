class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i+1, len(points)):
                xj, yj = points[j]
                dist = abs(yj-yi) + abs(xj-xi)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prims
        min_cost = 0
        visited = set()
        heap = [[0,0]] # [dist, node]
        while len(visited) < len(points):
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            min_cost += dist
            visited.add(node)
            for d,n in adj[node]:
                if n not in visited:
                    heapq.heappush(heap, [d, n])

        return min_cost
