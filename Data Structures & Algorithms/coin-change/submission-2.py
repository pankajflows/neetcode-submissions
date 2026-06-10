class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import cache
        @cache
        def rec(i, amt):
            if amt == 0:
                return 0
            elif amt < 0:
                return float("inf")
            if i >= len(coins):
                return float("inf")


            return min(
                1 + rec(i, amt-coins[i]), 
                rec(i+1, amt)
            )

        result = rec(0, amount)
        return result if result != float("inf") else -1
        