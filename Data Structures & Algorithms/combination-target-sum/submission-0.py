class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, arr):
            if arr and sum(arr) == target: ##### Constraints
                ans.append(arr)
                return False
            elif arr and sum(arr) > target: ##### Base case
                return False

            for i in range(len(nums)):
                backtrack(nums[i:], arr+[nums[i]]) ##### Choices

        ans = list()
        backtrack(nums, [])

        return ans





        