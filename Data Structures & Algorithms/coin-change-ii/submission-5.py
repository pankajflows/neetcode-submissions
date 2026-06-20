class Solution:
    def change22(self, amount: int, coins: List[int]) -> int:
        # recursive
        from functools import cache

        @cache
        def rec(i, total):
            if total == amount:
                return 1
            if i >= len(coins):
                return 0
            if total > amount:
                return 0

            return rec(i, total+coins[i]) + rec(i+1, total)

        return rec(0, 0)


    def change(self, amount: int, coins: List[int]) -> int:
        # bottom up

        # blank matrix
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]

        # boundary conditions
        for i in range(n+1):
            dp[i][amount] = 1

        # dp[-1][-1] = 0
        # print(dp)

        for i in range(len(coins)-1, -1, -1):
            for total in range(amount-1, -1, -1):
                take = 0
                if total + coins[i] <= amount:
                    take = dp[i][total + coins[i]]
                skip = dp[i+1][total]
                dp[i][total] = take + skip

        return dp[0][0]

        






        