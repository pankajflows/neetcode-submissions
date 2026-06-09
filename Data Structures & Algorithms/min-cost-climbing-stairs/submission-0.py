class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = dict()
        n = len(cost)

        def steps(i):
            if i in cache:
                return cache[i]
            if i >= n:
                return 0
            
            c = cost[i] + min(steps(i+1), steps(i+2))
            cache[i] = c
            return c

        return min(steps(0), steps(1))

