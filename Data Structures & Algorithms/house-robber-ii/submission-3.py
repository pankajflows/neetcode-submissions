class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(i, nums):
            if i >= len(nums):
                return 0
            if cache[i]:
                return cache[i]
            
            c = max(nums[i] + dp(i+2, nums), dp(i+1, nums))
            cache[i] = c
            return c
        print(nums[1:], nums[:-1])

        cache = [None]*len(nums)
        a = dp(0, nums[1:])
        cache = [None]*len(nums)
        b = dp(0, nums[:-1])
        return max(a, b)