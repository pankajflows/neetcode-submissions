class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxi = [0]*len(prices)
        loc_max = 0

        for i in range(len(prices)-1,-1,-1):
            loc_max = max(loc_max, prices[i])
            maxi[i] = loc_max
        print(maxi)

        ans = 0
        for i in range(len(prices)):
            ans = max(ans, maxi[i]-prices[i])

        return ans

        