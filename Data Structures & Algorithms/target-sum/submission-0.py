class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def rec(i, temp):
            if i >= n:
                if temp == target:
                    return 1
                else:
                    return 0
            

            # add current number
            a = rec(i+1, temp + nums[i])

            # subtract current number
            b = rec(i+1, temp - nums[i])

            return a+b

        return rec(0, 0)