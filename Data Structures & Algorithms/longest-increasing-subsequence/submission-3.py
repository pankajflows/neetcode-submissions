class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Observations
        # ------------
        # If i start with a number, the further selections will be greater than this
        #
        
        # recursion
        # from functools import cache
        # @cache
        def rec(i, j):
            if j != -1 and dp[i][j]:
                return dp[i][j]
            if i >= len(nums):
                return 0

            # what if I choose this number
            a = None
            if j == -1:
                a = 1 + rec(i+1, i)
            elif nums[i] > nums[j]:
                a = 1 + rec(i+1, i)

            # what if I skip this number
            b = rec(i+1, j)

            ret = b if not a else max(a,b)
            dp[i][j] = ret
            return ret

        dp = [[None for i in range(len(nums)+1)] for j in range(len(nums)+1)]
        ans = rec(0, -1)
        return ans
        