class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def rec(i, my_stock):
            if i >= len(prices):
                return 0

            if my_stock is None:
                # you either buy 
                a = rec(i+1, prices[i]) - prices[i]

                # or not buy
                b = rec(i+1, None)

                return max(a,b)

            else:
                # sell
                a = prices[i] + rec(i+2, None)

                # or not sell
                b = rec(i+1, my_stock)

                return max(a,b)

        return rec(0, None)






        