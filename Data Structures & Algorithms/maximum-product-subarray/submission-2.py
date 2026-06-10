class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mi = nums[0]
        mx = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            c1 = mi * n
            c2 = mx * n

            mx = max(n, c1, c2)
            mi = min(n, c1, c2)

            ans = max(ans, mx)
        
        return ans


    def maxProduct22(self, nums: List[int]) -> int:
        i = 0
        j = 0
        prod = None
        ans = None
        temp = None

        while i <= j and i < len(nums) and j < len(nums):
            print("start", i, j, temp, prod, ans)
            if prod is None:
                temp = nums[i]
                prod = temp
            else:
                temp = prod * nums[j]

            if temp >= prod:
                j += 1
                ans = max(ans, temp) if ans else temp
                prod = temp
            elif temp < prod:
                i = j+1
                j = i
                prod = None
            print("end", i, j, temp, prod, ans)

        return ans

            