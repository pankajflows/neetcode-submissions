class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(index_to_skip, arr):
            if len(arr) == len(nums):
                ans.append(arr.copy())
                return

            for i in range(len(nums)):
                if i in index_to_skip:
                    continue
                index_to_skip.add(i)
                backtracking(index_to_skip, arr+[nums[i]])
                index_to_skip.remove(i)


        index_to_skip = set()
        ans = list()
        backtracking(index_to_skip, [])
        return ans
        

