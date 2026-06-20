class Solution:
    def findTargetSumWays22(self, nums: List[int], target: int) -> int:
        # recursive
        n = len(nums)
        from functools import cache

        @cache
        def rec(i, temp):
            if i >= n:
                if temp == target:
                    return 1
                else:
                    return 0
            

            # add current number
            a = rec(i+1, temp + nums[i])

            # subtract current number
            b = rec(i+1, temp - nums[i])

            return a+b

        return rec(0, 0)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums):
            return 0
        n = len(nums)
        total_sum = offset = sum(nums)
        max_sum_range = total_sum*2+1
        dp = [[0]*(max_sum_range) for _ in range(n+1)]

        dp[n][target+offset] = 1

        for i in range(n-1, -1, -1):
            for temp in range(-total_sum, total_sum+1):
                if 0 <= temp+nums[i] + offset < max_sum_range:
                    dp[i][temp + offset] += dp[i+1][temp+nums[i] + offset]
                if 0 <= temp-nums[i] + offset < max_sum_range:
                    dp[i][temp + offset] += dp[i+1][temp-nums[i] + offset]

        return dp[0][0+offset]
















