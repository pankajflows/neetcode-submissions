class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start, end):
            if start == end:
                print(start, end)
                return start if nums[start] == target else -1

            mid = (start+end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(start, mid)
            else:
                return binary_search(mid+1, end)




        return binary_search(0, len(nums)-1)
        