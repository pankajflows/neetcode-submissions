class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        from functools import cache

        nums = [1] + nums + [1]
        def numsget(index):
            if index < 0 or index >= len(nums):
                return 1
            else:
                return nums[index]

        @cache
        def rec(left, right):
            if left+1 == right:
                return 0

            m = 0
            for k in range(left+1, right):
                a = rec(left, k) # burst
                b = rec(k, right) # not burst
                c = nums[left] * nums[k] * nums[right]
                m = max(m, a+b+c)
            return m

        return rec(0,len(nums)-1)
        