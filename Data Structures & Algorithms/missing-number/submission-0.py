class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        p = 0
        for i in range(1, len(nums)+1):
            p ^= i

        for n in nums:
            p ^= n

        return p