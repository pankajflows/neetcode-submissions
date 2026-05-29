class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(l, i):
            if i >= len(nums):
                ans.append(list(l))
                return
            
            # print("l, i", l, i)
            # print("ans", ans)

            # dont consider that number
            helper(l, i+1)

            # consider that number
            l.append(nums[i])
            helper(l, i+1)
            l.pop(-1)


        ans = list()
        temp = []
        helper(temp, 0)
        return ans

        