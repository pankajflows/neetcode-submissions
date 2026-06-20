class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
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






        