class Solution:
    def climbStairs(self, n: int) -> int:
        cache = dict()
        def steps(n):
            if n in cache:
                return cache[n]
            if n == 0:
                return 1
            elif n < 0:
                return 0
            c = steps(n-1) + steps(n-2)
            cache[n] = c
            return c

        return steps(n)