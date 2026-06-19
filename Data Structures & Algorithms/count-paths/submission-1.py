class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]
        def rec(i,j):
            if dp[i][j]:
                return dp[i][j]
            if i >= m or j >= n:
                return 0
            elif i == m-1 and j == n-1:
                return 1

            p = rec(i, j+1) + rec(i+1, j)
            dp[i][j] = p
            return p

        return rec(0,0)
        


