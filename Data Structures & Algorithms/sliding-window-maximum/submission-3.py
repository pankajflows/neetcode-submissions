class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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