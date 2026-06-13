class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Observations
        # ------------
        # If I choose a number at position i in subset1 then that number will not be there in subset2
        
        def rec(sum1, i):
            if i >= len(nums):
                return False
            if sum1 == real_sum1:
                return True
            elif sum1 > real_sum1:
                return False

            # choose the current number
            if rec(sum1+nums[i], i+1):
                return True

            # do not choose the current number
            if rec(sum1, i+1):
                return True

            return False

        real_sum1 = sum(nums)/2
        return rec(0, 0)


