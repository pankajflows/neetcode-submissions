class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bank = dict()

        for n in nums:
            if n in bank:
                return True
            else:
                bank[n] = 1

        return False
        