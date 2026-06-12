class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Observations
        # ------------
        # If i start with a number, the further selections will be greater than this
        #
        
        # recursion
        from functools import cache
        @cache
        def rec(i, prev):
            # print(i, count, prev)
            if i >= len(nums):
                # ans[0] = max(ans[0], count)
                return 0

            # what if I choose this number
            a = None
            if nums[i] > prev:
                a = 1 + rec(i+1, nums[i])

            # what if I skip this number
            b = rec(i+1, prev)

            return b if not a else max(a,b)

        ans = [0]
        a = rec(0, -float("inf"))
        return a
        