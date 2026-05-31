class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, arr):
            ans.append(arr.copy())
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                # Take
                arr.append(nums[j])
                backtrack(j+1, arr)
                arr.pop()

                # not take
                # backtrack(i+1, arr)


        nums.sort()
        ans = list()
        backtrack(0, [])
        return ans

        