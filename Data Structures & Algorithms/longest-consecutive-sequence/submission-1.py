class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make a hashset
        # loop through nums one by one
        # of num-1 exist, then it not start of a sequence
        # if num-1 doesnt exist its start of a sequence
        # loop by doing membership check on num+1 and obtain max

        if len(nums) == 0:
            return 0
        hashset = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in hashset:
                tc = 0
                num += 1
                while num in hashset:
                    tc += 1
                    ans = max(ans, tc)
                    num += 1

        return ans+1


        