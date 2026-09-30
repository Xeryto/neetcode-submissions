class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if len(self.maxheap) <= len(self.minheap):
            if not self.minheap or num <= self.minheap[0]:
                heapq.heappush(self.maxheap, num*-1)
            else:
                temp = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -1*temp)
                heapq.heappush(self.minheap, num)
        else:
            if num > self.maxheap[0]*-1:
                heapq.heappush(self.minheap, num)
            else:
                temp = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -1*temp)
                heapq.heappush(self.maxheap, num*-1)
            

    def findMedian(self) -> float:
        ans = 0
        if len(self.maxheap) > len(self.minheap):
            ans = self.maxheap[0]*-1
        elif len(self.maxheap) < len(self.minheap):
            ans = self.minheap[0]
        else:
            ans = (self.maxheap[0]*(-1)+self.minheap[0])/2
        
        return ans


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()