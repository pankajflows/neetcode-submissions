class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import cache
        @cache
        def rec(i, coin, amt):
            if amt == 0:
                return coin
            elif amt < 0:
                return float("inf")
            if i >= len(coins):
                return float("inf")


            return min(
                rec(i, coin+1, amt-coins[i]), 
                rec(i+1, coin, amt)
            )

        result = rec(0, 0, amount)
        return result if result != float("inf") else -1
        