class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # recursive
        dp = [[None for _ in range(n)] for _ in range(m)]
        def rec(i,j):
            if i >= m or j >= n:
                return 0
            if dp[i][j]:
                return dp[i][j]
            elif i == m-1 and j == n-1:
                return 1

            p = rec(i, j+1) + rec(i+1, j)
            dp[i][j] = p
            return p

        return rec(0,0)
        

    def uniquePaths11(self, m: int, n: int) -> int:
        pass

