class Solution:
    def uniquePaths22(self, m: int, n: int) -> int:
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
        

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                # print("at", i,j, dp[i+1][j], dp[i][j+1])
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        print(dp)
        return dp[0][0]