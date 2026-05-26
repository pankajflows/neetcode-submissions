class Solution:
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(a,b):
            return math.sqrt((a*a) + (b*b))

        heap = list()
        for point in points:
            heap.append(
                (-dist(point[0], point[1]), point[0], point[1])
            )

        heapq.heapify(heap)

        ans = list()
        # print(heap)
        while len(heap) > k:
            heapq.heappop(heap)

        # print(heap)
        while heap:
            d, a, b = heapq.heappop(heap)
            ans.append([a,b])

        return ans

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = list()
        for point in points:
            area = math.sqrt((point[0]*point[0]) + (point[1]*point[1]))
            if len(heap) >= k:
                heapq.heappushpop(heap, (-area, point[0], point[1]))
            else:
                heapq.heappush(heap, (-area, point[0], point[1]))

        return [[p[1], p[2]] for p in heap]


        