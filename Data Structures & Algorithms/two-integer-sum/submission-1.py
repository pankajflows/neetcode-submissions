class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1

        while i < j:
            s = nums[i] + nums[j]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return [i,j]
        return [0,0]

    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]] if i < hashmap[diff] else [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i




