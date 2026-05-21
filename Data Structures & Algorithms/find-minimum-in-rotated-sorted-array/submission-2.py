class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        ans = -1
        loc_mid = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] > nums[mid]:
                right = mid - 1
                loc_mid = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
                loc_mid = mid
            else:
                ans = min(nums[loc_mid], nums[left], nums[right], nums[mid])
                break

        print("ans", ans, left, right)
        return ans
        