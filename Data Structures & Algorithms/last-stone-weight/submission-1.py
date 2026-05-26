class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        # print("before", stones)
        heapq.heapify(stones)
        # print("after", stones)

        while stones:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones) 
            else:
                return -x

            smash = abs(abs(x) - abs(y))
            heapq.heappush(stones, -smash)

        return 0
        