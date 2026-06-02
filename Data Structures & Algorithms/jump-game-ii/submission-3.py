class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        ans = 0
        l = r = 0

        while r < len(nums)-1:
            mx = 0
            for i in range(l, r+1):
                if mx < i+nums[i]:
                    mx = i+nums[i]
            ans += 1

            l = r+1
            r = mx


        return ans


