class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        submaxi = nums[0]
        maxi = nums[0]

        for i in range(1, len(nums)):
            submaxi = max(nums[i], submaxi + nums[i])
            maxi = max(maxi, submaxi)
        
        return maxi

        