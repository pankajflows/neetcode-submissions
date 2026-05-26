class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        self.k = k
        while len(self.nums) > self.k:
            heapq.heappop(nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        k = self.k
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
        
