class MedianFinder:

    def __init__(self):
        self.lheap = list()
        self.rheap = list()

    
    def topl(self):
        # return max of selh.lheap in positive
        if not self.lheap:
            return
        return -self.lheap[0]

    
    def topr(self):
        if not self.rheap:
            return
        return self.rheap[0]
        

    def addNum(self, num: int) -> None:
        l = self.lheap
        r = self.rheap
        topl = self.topl
        topr = self.topr

        if not self.lheap or num <= topl():
            heapq.heappush(self.lheap, -num)
        else:
            heapq.heappush(self.rheap, num)

        if len(self.lheap) > len(self.rheap) + 1:
            orphan = -heapq.heappop(self.lheap)
            heapq.heappush(self.rheap, orphan)
        if len(self.rheap) > len(self.lheap):
            orphan = heapq.heappop(self.rheap)
            heapq.heappush(self.lheap, -orphan)
            

    def findMedian(self) -> float:
        l = self.lheap
        r = self.rheap
        topl = self.topl
        topr = self.topr
        ln = len(l)
        rn = len(r)

        if ln <= rn:
            return (topl() + topr()) / 2
        else:
            return topl()
        
        