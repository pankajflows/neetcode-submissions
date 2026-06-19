class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import cache
        @cache
        def rec(i,j):
            if i >= m or j >= n:
                return 0
            elif i == m-1 and j == n-1:
                return 1

            a = rec(i, j+1)
            b = rec(i+1, j)
            return a + b

        return rec(0,0)
        


