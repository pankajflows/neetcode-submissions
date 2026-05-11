class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p1 = [0]*len(nums)
        p2 = [0]*len(nums)
        ans = list()

        for i in range(len(nums)):
            if i == 0:
                p1[i] = 1
                continue
            p1[i] = p1[i-1] * nums[i-1]
        # [1,2,4,6]
        # [0,1,]

        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                p2[i] = 1
                continue
            p2[i] = p2[i+1] * nums[i+1]

        print(p1)
        print(p2)

        for i in range(len(nums)):
            if i == 0:
                ans.append(p2[i])
            elif i == len(nums) - 1:
                ans.append(p1[i])
            else:
                ans.append(p1[i] * p2[i])

        return ans

        