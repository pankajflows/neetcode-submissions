class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        while k > 0:
            k -= 1
            ans = -heapq.heappop(nums)

        return ans
        