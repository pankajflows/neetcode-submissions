class Solution:
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        # Using a heap 
        heap = [(-v,k) for k,v in enumerate(nums[:k])]
        heapq.heapify(heap)
        loc_max = heap[0]
        ans = [0]*(len(nums)-k+1)
        ans[0] = -loc_max[0]
        i = 1
        j = i+k-1
        # print("start heap", heap)

        while j < len(nums):
            incoming = nums[j]
            outgoing = nums[i]

            heapq.heappush(heap, (-incoming, j))

            while heap and heap[0][1] <= j-k:
                ele = heapq.heappop(heap)

            ans[j-k+1] = -heap[0][0]

            i += 1
            j += 1
        # print("ans raw", ans)
        # return [-a[0] for a in ans]
        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monodec = deque()
        ans = list()

        # front - right
        # back - left

        for i in range(len(nums)):
            # pop elements from left if they are outside current window i-k
            while monodec and monodec[-1] <= i-k:
                monodec.pop()

            # pop elments from right to maintain decresing deque
            while monodec and nums[monodec[0]] <= nums[i]:
                monodec.popleft()

            # push current element in deque
            monodec.appendleft(i)

            # push top of queue to ans if k elements are laready processed
            if i >= k-1:
                ans.append(nums[monodec[-1]])

        return ans

        