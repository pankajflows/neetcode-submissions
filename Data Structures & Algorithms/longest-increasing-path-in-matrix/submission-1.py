class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        from functools import cache

        @cache
        def rec(i,j):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return 0

            up = rec(i-1, j) if i-1 >= 0 and matrix[i-1][j] > matrix[i][j] else 0
            down = rec(i+1, j) if i+1 < len(matrix) and matrix[i+1][j] > matrix[i][j] else 0
            left = rec(i, j-1) if j-1 >= 0 and matrix[i][j-1] > matrix[i][j] else 0
            right = rec(i, j+1) if j+1 < len(matrix[0]) and matrix[i][j+1] > matrix[i][j] else 0

            return 1 + max(up, down, left, right)

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, rec(i,j))
        return ans

        