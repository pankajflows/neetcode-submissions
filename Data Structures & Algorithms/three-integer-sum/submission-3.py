class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            a = nums[i]
            j = i+1
            k = len(nums)-1

            while j < k:
                b = nums[j]
                c = nums[k]

                if a + b + c == 0:
                    print(a,b,c)
                    ans.add(tuple(sorted([a,b,c])))
                    j += 1
                elif a + b + c > 0:
                    k -= 1
                else:
                    j += 1
        print(ans)
        # return [[]]
        return [list(a) for a in ans]